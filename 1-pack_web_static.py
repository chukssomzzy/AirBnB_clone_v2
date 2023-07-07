#!/usr/bin/python3
""" Archive web_static """

from fabric import task
from fabric.api import local
from datetime import datetime


@task
def do_pack():
    """Run tar on localmachine"""
    cur_date = datetime.now()
    archive_name = cur_date.strftime('web_static_%Y%m%d%H%M%S')
    local("mkdir versions")
    local(f"tar -cvsf versions/{archive_name} web_static")
