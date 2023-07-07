#!/usr/bin/python3
""" Archive web_static """

from fabric import task
from datetime import datetime


@task
def do_pack(c):
    """Run tar on localmachine"""
    cur_date = datetime.now()
    archive_name = cur_date.strftime('web_static_%Y%m%d%H%M%S')
    c.local("mkdir versions")
    c.local(f"tar -cvsf versions/{archive_name} web_static")
