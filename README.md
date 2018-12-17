## Private Repo Migration

#### Prerequisits 

You need a system with make, python and pip in working order to proceed.  

#### Install

* `git clone https://github.com/xcsrz/private-repo-migration.git`
* `cd private-repo-migration`
* `make config`

#### Configure Credentials

This expects the following environment variables to be configured.

* `GITHUB_USER`
* `GITHUB_PASS`
* `BITBUCKET_USER`
* `BITBUCKET_PASS`

The best practice method of handling this is to create a temporary file:

```
export GITHUB_USER="Your Github Username Here"
export GITHUB_PASS="Your Github Password Here"
export BITBUCKET_USER="Your Bitbucket Username Here"
export BITBUCKET_PASS="Your Bitbucket Password Here"
```

Then load this into your session with `source creds.sh` (or whatever you named your credentials file).

*This should not be in your `.bashrc`/`.bash_profile` file and you should delete this file after you're done using it*

#### Running

`make run`