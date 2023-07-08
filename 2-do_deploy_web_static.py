#!/usr/bin/python3

"""distributes an archive to your web servers"""

from fabric.api import env, run, put
import os.path
env.hosts = ["54.160.79.245", '18.234.129.129']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Push local archieve to remote server """
    localfile = './versions/web_static_20230708143924.tgz'
    remo_releases = '/data/web_static/releases/web_static_20230708143924/'
    tmp_arch = '/tmp/web_static_20230708143924.tgz'
    repo_cur = '/data/web_static/current'
    if not archive_path or not os.path.isfile(archive_path):
        return False
    try:
        put("{}".format(localfile), "/tmp/")
        run("mkdir -p {}".format(remo_releases))
        run("tar -xzf {} -C {}".format(tmp_arch, remo_releases))
        run("rm {}".format(tmp_arch))
        run("mv {}web_static/* {}".format(remo_releases, remo_releases))
        run("rm -rf {}web_static".format(remo_releases))
        run("rm -rf {}".format(repo_cur))
        run("ln -s {} {}".format(remo_releases, repo_cur))
        print("New version deployed!")
        return True
    except Exception:
        return False
