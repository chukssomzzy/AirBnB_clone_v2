#!/usr/bin/env bash
# setup webserver for deployment of webstatic
DIR_DATA="/data"
DIR_RELEASE="$DIR_DATA/web_static/releases"
DIR_TEST="$DIR_DATA/web_static/releases/test"
DIR_SHARED="$DIR_TEST/web_static/shared"
DIR_CUR="$DIR_DATA/web_static/current"
USER_CONF="ubuntu"
NGINX_CONF="/etc/nginx/nginx/sites_available/"
NGINX_ENABLED="/etc/nginx/sites_enabled"

# upgrase the system
apt-get upgrade

# install nginx 
apt-get install nginx

# mkdir for test
mkdir -p $DIR_TEST

# mkdir for shared 
mkdir -p $DIR_SHARED

# create fake html file
if ! [[ -s "$DIR_TEST/index.html" ]]; then
cat << EOT >> "$DIR_TEST/index.html"
<html>
<head>
<title>
Fake Html Content
</title>
</head>
<body>
<h1> Fake Html Content </h1>
</body>
</html>
EOT
fi

# symbolic link  
ln -s -f $DIR_TEST $DIR_TEST

# chown 
chown -R $USER_CONF:$USER_CONF $DIR_DATA

# update nginx 

cat << EOT >> "$NGINX_CONF/www.somzzy.tech"
server {
    server_name somzzy.tech www.somzzy.tech;

    location /hbnb_static/ {
    alias $DIR_CUR
}
}
EOT
ln -s "$NGINX_CONF/www.somzzy.tech" "$NGINX_ENABLED/www.somzzy.tech"

nginx -s reload 
exit 0
