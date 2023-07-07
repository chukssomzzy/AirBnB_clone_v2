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
    try:
        if not os.path.isdir(dir_name):
            local("mkdir versions")
            local(f"tar -cvzf {dir_name}/{archive_name} web_static")
            return f"{dir_name}/{archive_name}"
    except Exception:
        return None
