# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *

env.user = 'ubuntu'
env.key_filename = ['/home/gabriel/keys/VMC.pem']

env.roledefs = {
    'prod': ['valpomobileconf.com'],
    }


def upload(msg="."):
    local('git pull')
    cmd = 'git add -A && git commit -am "%s"' % msg
    local(cmd)
    local('git push')


@roles('prod')
def deployprod():
    code_dir = 'vmcweb'
    with cd(code_dir):
        result = run("git pull")
        if 'requirements.txt' in str(result):
            run("sudo pip install -U -r requirements.txt")
        if not result.failed:
            packages = ['main']
            for pkg in packages:
                cmd = "./manage.py migrate %s" % pkg
                migrate_result = run(cmd)
                if migrate_result.failed:
                    run("./manage.py makemigrations --merge")
                    run(cmd)
            run("./manage.py collectstatic --noinput")
            run("./manage.py migrate")
        run("sudo supervisorctl restart vmc")


@roles('prod')
def deploy():
    code_dir = 'testing'
    with cd(code_dir):
        result = run("git pull")
        if 'requirements.txt' in str(result):
            run("sudo pip install -U -r requirements.txt")
        if not result.failed:
            packages = ['main']
            for pkg in packages:
                cmd = "./manage.py migrate %s" % pkg
                migrate_result = run(cmd)
                if migrate_result.failed:
                    run("./manage.py makemigrations --merge")
                    run(cmd)
            run("./manage.py collectstatic --noinput")
            run("./manage.py migrate")
        run("sudo supervisorctl restart testing")


@roles('prod')
def upgradeserver():
    run("sudo apt-get update")
    run("sudo apt-get dist-upgrade")
    run("sudo apt-get autoremove")


@roles('prod')
def installpkgs(pkg_names):
    cmd = "sudo pip install %s" % pkg_names
    run(cmd)
