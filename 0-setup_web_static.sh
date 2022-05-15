#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/error_page 404 \/custom_404.html;/ a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
