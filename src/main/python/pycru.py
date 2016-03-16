import argparse
import getpass
import io
import re
import requests

parser = argparse.ArgumentParser('pycru', description='Add git commits to Crucible reviews')
parser.add_argument('url', metavar='<url>', help='Crucible API URL to connect to')
parser.add_argument('username', metavar='<username>', help='The username for logging in to Crucible')
parser.add_argument('repository', metavar='<repo>', help='The name of the git repository as configured on the Crucible server')
parser.add_argument('review_id', metavar='<review-id>', help='The id of the review to add the revisions to')
args = parser.parse_args()

valid_commit_id = re.compile('^[a-fA-F0-9]+$')
commits = io.open(0, 'rt', closefd=False).readlines()
if (not all(valid_commit_id.match(commit) for commit in commits)):
    print('Invalid commit ids specified')
    exit(1)

login = requests.post(args.url + '/rest-service-fecru/auth/login', 
                      data={'userName': args.username, 'password':getpass.getpass()})
if (login.status_code != 200):
    print('Login failed')
    exit(1)
token = login.json()['token']
    
request = {
    'repository': args.repository,
    'changesets': {
        'changesetData': [{'id': commit.strip()} for commit in commits]
    }
}
addChangesets = requests.post(args.url + '/rest-service/reviews-v1/' + args.review_id + '/addChangeset', 
                              params={'FEAUTH': token}, 
                              json=request)
                              
if (addChangesets.status_code != 200):
    print('Adding changesets failed')
    exit(1)
