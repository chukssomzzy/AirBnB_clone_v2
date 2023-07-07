#!/usr/bin/python3
""" Archive web_static """

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """Run tar on localmachine"""
    cur_date = datetime.now()
    archive_name = cur_date.strftime('web_static_%Y%m%d%H%M%S.tgz')
    dir_name = 'versions'
    if not os.path.isdir(dir_name):
        if local("mkdir versions").failed:
            return None
    if local(f"tar -cvsf {dir_name}/{archive_name} web_static").failed:
        return None
    return archive_name
