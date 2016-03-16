# pycru
Command-line Python script which adds the specified git commits to a Crucible review

## Usage

    pycru [-h] <url> <username> <repo> <review-id>

* `-h`: Show the help documentation.
* `<url>`: The URL of the Crucible server to upload your commits to. The URL should not have any trailing slashes.
* `<username>`: Username used to login into the specified Crucible server. You will be asked for your password separately after you run the script.
* `<repo>`: The repository name to get commits from, as configured on the Crucible server.
* `<review-id>`: The review ID which will be updated with the revisions passed in on the input stream.

The script will login into the specified Crucible server on the URL, using the specified username and password (entered after you run the script) and add the input commits/revisions, taken from the specified repository, to the specified open review. You must specify the list of commit/revision IDs to add on the standard input stream.

For example, the following command will upload all on the current git branch but not on the `develop` branch to the review with ID REV-203:

    git rev-list develop..HEAD | pycru https://test.crucibletest.com john.doe MainProjectRepo REV-203

Enjoy!

## Contribute

Help make this script better! Feel free to submit your improvements as pull requests.
