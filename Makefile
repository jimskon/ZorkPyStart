#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

user = skon

all:  PutHTML PutCGI

PutCGI:
		chmod 757 gamewebclient.py
		cp gamewebclient.py /usr/lib/cgi-bin/$(user)_gamewebclient.py

		echo "Current contents of your cgi-bin directory: "
		ls -l /usr/lib/cgi-bin/

PutHTML:
	cp zork.html /var/www/html/class/softdev/$(user)/pyGame/
	cp zork.css /var/www/html/class/softdev/$(user)/pyGame/
	cp zork.js /var/www/html/class/softdev/$(user)/pyGame/
	cp favicon.ico /var/www/html/class/softdev/$(user)/pyGame/
	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(user)/pyGame/
