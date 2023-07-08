#!/usr/bin/python3
""" Archive web_static """

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """Run tar on localmachine"""
    cur_date = datetime.utcnow()
    date_tar = cur_date.strftime('%Y%m%d%H%M%S')
    dir_name = 'versions'
    filepath = "{}/web_static_{}.tgz".format(dir_name, date_tar)
    try:
        if not os.path.isdir(dir_name):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(filepath))
        return filepath
    except Exception:
        return None
