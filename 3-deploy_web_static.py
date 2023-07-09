#!/usr/bin/python3

"""Full deploy of webstatic"""


def deploy():
    """Full deploy of webstatic"""
    do_deploy = __import__("./2-do_deploy_web_static.py").do_pack
    do_pack = __import__("./1-pack_web_static.py").do_pack

    archive_path = do_pack()
    if archive_path:
        if do_deploy(archive_path=archive_path):
            return True
    return False
