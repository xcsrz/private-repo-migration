import os
from github import Github
from bitbucket.bitbucket import Bitbucket
from subprocess import call


gh = Github(os.environ['GITHUB_USER'], os.environ['GITHUB_PASS'])
bb = Bitbucket(os.environ['BITBUCKET_USER'], os.environ['BITBUCKET_PASS'])

os.mkdir('repos')
os.chdir('repos')
for repo in gh.get_user().get_repos():
    # only worry about our own
    if repo.owner.login == os.environ['GITHUB_USER']:
        # only worry about private repos
        if repo.private:
            print "grabbing %s/%s" % (repo.owner.login, repo.name)
            call(["git", "clone", "--mirror", repo.ssh_url])
            os.chdir(repo.name+".git")
            success, result = bb.repository.create(repo.name, scm='git', private=True)
            if not success:
                raise Exception(result)
            call(['git','remote','set-url','origin','git@bitbucket.org:%s/%s.git' % (os.environ['BITBUCKET_USER'], repo.name)])
            print "uploading %s/%s" % (os.environ['BITBUCKET_USER'], repo.name)
            call(["git", "push", "--mirror", "origin"])
            os.chdir('..')
