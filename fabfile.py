# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *

env.user = 'ubuntu'
env.key_filename = ['/home/gabriel/keys/MobileConf.pem']

env.roledefs = {
    'prod': ['valpomobileconf.com'],
    }


def upload(msg="."):
    local('git pull')
    cmt = 'git add -A && git commit -am "%s"' % msg
    local(cmt)
    local('git push')

@roles('prod')
def pull():
    code_dir = 'vmcweb'
    with cd(code_dir):
        result = run("git pull")
        if not result.failed:
            if 'migrations/' in str(result):
                run("./manage.py migrate")
            if ('.png' in str(result)) or ('.jpg' in str(result)) or \
                ('.css' in str(result)) or ('.js' in str(result)):
                run("./manage.py collectstatic --noinput")
            if ('.py' in str(result) or '.mo' in str(result)):
                run("sudo reboot")


@roles('prod')
def betaupgrade():
    run("sudo apt-get update")
    run("sudo apt-get dist-upgrade")
    run("sudo apt-get autoremove")


@roles('prod')
def installpkgs(pkg_names):
    cmd = "sudo pip install %s" % pkg_names
    run(cmd)