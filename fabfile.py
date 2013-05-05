from __future__ import with_statement
from fabric.api import local, cd, run, lcd

def init_repo():
        local('git init')

def start_project(project_name):
    #local('django-admin.py startproject --template=https://github.com/rbeagrie/django-twoscoops-project/zipball/master --extension=py,rst,html %s' % project_name)
    local('django-admin.py startproject %s' % project_name)

def create_project(project_name):
    start_project(project_name)
    with lcd(project_name):
	    init_repo()
	    first_commit()

def first_commit():
    local('git add . && git commit -am "First commit"')
