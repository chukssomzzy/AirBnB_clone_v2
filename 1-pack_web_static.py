#!/usr/bin/python3
""" Archive web_static """

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Run tar on localmachine"""
    cur_date = datetime.now()
    archive_name = cur_date.strftime('web_static_%Y%m%d%H%M%S')
    dir_name = 'version'
    if not os.path.isdir(dir_name):
        if local("mkdir versions").failed:
            return None
    if not local(f"tar -cvsf versions/{archive_name} web_static"):
        return None
    return archive_name
