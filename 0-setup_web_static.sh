#!/usr/bin/env bash
# setup webserver for deployment of webstatic
DIR_DATA="/data"
DIR_TEST="$DIR_DATA/web_static/releases/test"
DIR_SHARED="$DIR_DATA/web_static/shared"
DIR_CUR="$DIR_DATA/web_static/current"
USER_CONF="ubuntu"
NGINX_CONF="/etc/nginx/sites-available/"
NGINX_ENABLED="/etc/nginx/sites-enabled"

# upgrase the system
apt-get update

# install nginx 
apt-get -y install nginx

# mkdir for test
mkdir -p $DIR_TEST

# mkdir for shared 
mkdir -p $DIR_SHARED

mkdir -p $DIR_CUR

# create fake html file
if ! [[ -s "$DIR_TEST/index.html" ]]; then
cat << EOT >> "$DIR_TEST/index.html"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOT
fi

# symbolic link  
ln -s -f $DIR_TEST $DIR_TEST

# chown 
chown -R $USER_CONF:$USER_CONF $DIR_DATA

# update nginx 
if ! [[ -s "$NGINX_CONF/somzzy.tech" ]]; then
cat << EOT >> "$NGINX_CONF/somzzy.tech"
server {
    server_name somzzy.tech www.somzzy.tech;

    location /hbnb_static/ {
        alias $DIR_CUR;
    }

    add_header X-Served-By 152562-web-02;
}
EOT
fi 

if ! [[ -h "$NGINX_ENABLED/somzzy.tech" ]]; then
ln -s "$NGINX_CONF/somzzy.tech" "$NGINX_ENABLED"
fi

sed -i "s/#server_na.*_size\s64;/server_names_hash_bucket_size 64;/1" "/etc/nginx/nginx.conf" 

if  nginx -t; then
service nginx restart 
exit 0
fi 
exit 1
