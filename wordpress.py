import os 
import sys

if str(os.getuid()) == "1000":
    print()
    print()
    print()
    print()
    print()
    print("please run this program as root") 
    print()
    print()
    print()
    print()
    print()
    sys.exit()

while 1==1:
	print()
	print()
	print()
	print()
	print()
	print("1) update system")
	print("2) install php 7.4")
	print("3) install apache2")
	print("4) install mariadb")
	print("5) config mariadb")
	print("6) install wordpress")
	print()
	

	choix = input("choix : ")

	if choix == str(1):
		print()
		os.system("sudo apt-get update && apt-get upgrade")
	elif choix == str(2):
		print()
		os.system("sudo add-apt-repository ppa:ondrej/php")
		os.system('sudo apt-get update')
		os.system("sudo apt install php8.1")
		os.system("sudo apt-get install php-mysql")
		os.system("sudo apt install php8.1-mysql")
	elif choix == str(3):
		os.system("sudo apt-get install apache2")
	elif choix == str(4):
		os.system("sudo apt-get install mariadb-server")
		print()
		print()
		print('answer "y" to all questions (press enter to continue ...)')
		print()
		print()
		os.system("sudo mysql_secure_installation")
	elif choix == str(5):
		print()
		user = input("chose a user name for your database : ")
		password = input("chose a password for your database : ")
		print()
		print()
		print("open a new terminal and copy & past following lines one by one  : ")
		print()
		print()
		print()
		print("sudo mysql -uroot -p")
		print("CREATE DATABASE wordpress;")
		print("CREATE USER '"+ user +"'@'localhost' IDENTIFIED BY '"+ password +"';")
		print("GRANT ALL PRIVILEGES ON wordpress.* TO '"+ user +"'@'localhost';")
		print("FLUSH PRIVILEGES;")
		print("exit")
	elif choix == str(6):
		os.system("cd /var/www/html/ && sudo wget https://wordpress.org/latest.zip -O /var/www/html/wordpress.zip && sudo unzip wordpress.zip && sudo chmod 755 wordpress -R && sudo chown www-data wordpress -R")
		print()
		print()
		print()
		choix = input("install is down ! do you want to reboot now ? (y/n)")
		print()
		print()
		print()
		if choix == str("y"):
			os.system("sudo reboot")
		sys.exit()
