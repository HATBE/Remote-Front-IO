sudo apt update && sudo apt upgrade

apit install git -y
sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y

sudo rm /var/www/html/index.html
cd /var/www/html/
sudo git clone https://github.com/HATBE/Remote-Front-IO.git .

sudo chown www-data:www-data /var/www/html -R
sudo chmod 755 /var/www/html -R

sudo nano /etc/apache2/sites-available/000-default.conf

->
 DocumentRoot /var/www/html/web
<-

sudo systemctl reload apache2

sudo visudo

->
www-data ALL=(ALL) NOPASSWD: /usr/bin/python /var/www/html/power.py power
www-data ALL=(ALL) NOPASSWD: /usr/bin/python /var/www/html/power.py powerhard
www-data ALL=(ALL) NOPASSWD: /usr/bin/python /var/www/html/power.py reset
<-

sudo nano /etc/systemd/system/rfio.service

->
[Unit]
Description=isUp service

[Service]
WorkingDirectory=/var/www/html
User=www-data
Group=www-data
Restart=always
ExecStart=sudo /usr/bin/python /var/www/html/isUp.py

[Install]
WantedBy=multi-user.target
<-

sudo systemctl enable rfio
sudo systemctl start rfio