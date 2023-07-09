# configure webstatic and setup nginx 

$htmlcontent = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
$nginxconfig = "server {

    listen 80 default_server;
    listen [::]:80 default_server;

    location /hbnb_static/ {
        alias '/data/web_static/current/';
        autoindex off;
    }

    location / {
        root /var/www/html;
        index index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;

    location = /404.html{
         internal;
    }


    add_header X-Served-By ${hostname};
}
 "


file {'/data/web_static/':
  ensure => directory
}

file {'/data/web_static/releases/':
  ensure => directory
}

file {'/data/web_static/shared/':
  ensure => directory
}

file {'/data/web_static/releases/test/':
  ensure => directory
}

file {'/data/web_static/releases/test/index.html':
  ensure  => file,
  content => $htmlcontent
}

file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/'
}


file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => nginxconfig,
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => 'true'
  }
