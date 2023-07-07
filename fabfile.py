#!/usr/bin/python3
""" Archive web_static """

from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """Run tar on localmachine"""
    cur_date = datetime.now()
    archive_name = cur_date.strftime('web_static_%Y%m%d%H%M%S')
    dir_name = 'version'
    if not os.path.isdir(dir_name):
        if c.local("mkdir versions").failed:
            return None
    if not c.local(f"tar -cvsf versions/{archive_name} web_static"):
        return None
    return archive_name
