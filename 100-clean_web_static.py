#!/usr/bin/python3

"""Cleanup outofdate archive file"""
from fabric.api import local, lcd, env, cd, run
import os

env.hosts = ["web-01.somzzy.tech", "web-02.somzzy.tech"]


def do_clean(number=0):
    """Cleanup archive file"""
    number = int(number)
    number = (number == 0 or number == 1) and 1 or number
    archive_path = "versions/"
    archive_sorted = sorted(os.listdir(archive_path), reverse=True)

    with lcd("versions/"):
        for file in archive_sorted[:-number]:
            local("rm -rf {}".format(file))
    with cd("/data/web_static/releases"):
        dirList = run("ls -rt").split()
        for file in dirList[:-number]:
            if file.startswith("web_static_"):
                run("rm -rf {}".format(file))
