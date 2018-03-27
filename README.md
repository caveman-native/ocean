# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Install python and pip
* install bottle (pip install bottle)
* or copy bottle.py at installation directory
* Database configuration - pip install tinydb
* How to run tests
* Deployment instructions

### deploy bottle to apache ###

* State apache - systemctl start httpd.service
* Enable apache - systemctl enable httpd.service
* Open apache - firewall-cmd --permanent --add-service=http or firewall-cmd --add-service=http
* Create a directory at var\www\newdirectory e.g. var\new\ocean
* 
* In Debian:
* Install wsgi - apt-get install libapache2-mod-wsgi
* Check if wsgi enabled:
  pache2ctl -M|grep -i wsgi
  Syntax OK
  wsgi_module (shared)
* Create configuration file - touch /etc/apache2/sites-available/schedule.conf
  Sample file:
  <VirtualHost *:80>
    ServerName www.schedule.com

    WSGIScriptAlias / /root/ocean/ocean/ocean.wsgi
    <Directory /root/ocean/ocean/>
        Require all granted
     </Directory>

  </VirtualHost>


* Add new conf to site enabled using - a2ensite schedule.conf
* Check configuration - apache2ctl configtest

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact