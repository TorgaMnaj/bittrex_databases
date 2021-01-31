#!/bin/bash

echo -e "

			INITIAL DATABASES:

This will take you through a series of prompts where you can make some changes to
your MariaDB installation’s security options.


1.	The first prompt will ask you to enter the current database root password. Since
	you have not set one up yet, press ENTER to indicate 'none'.

2.	The next prompt asks you whether you’d like to set up a database root password.
	On Ubuntu, the root account for MariaDB is tied closely to automated system
	maintenance, so we should not change the configured authentication methods for
	that account. Doing so would make it possible for a package update to break the
	database system by removing access to the administrative account. Type N and then
	press ENTER.

3.	From there, you can press Y and then ENTER to accept the defaults for all the
	subsequent questions. This will remove some anonymous users and the test
	database, disable remote root logins, and load these new rules so that MariaDB
	immediately implements the changes you have made.

ENTER TO CONTINUE....
"
read -r > /dev/null
sudo mysql_secure_installation
clear
echo -e "

			NOW DO THIS:

To this end, we will create a new account called admin with the same capabilities
as the root account, but configured for password authentication. Open up the
MariaDB prompt from your terminal:

	sudo mariadb

Then create a new user with root privileges and password-based access. Be sure to
change the username and password to match your preferences:

	GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

Flush the privileges to ensure that they are saved and available in the current
session:

	FLUSH PRIVILEGES;

Following this, exit the MariaDB shell:

	exit


ENTER TO CONTINUE....
"
read -r > /dev/null
sudo mariadb
clear
echo -e "
	PRINTING STATUS:
"
sudo systemctl start mariadb
sudo systemctl status mariadb
sudo mysqladmin version
echo -e "

ENTER TO CONTINUE....

"
read -r > /dev/null

clear
echo -e "

	Now checking user access---

ENTER:

sudo -u user mysqladmin -u user -p version

"

exit 0
