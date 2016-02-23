import time
import os


os.system("cd /var/www/")

num = 1
while num == 1:
	print("pulling from github")
	os.system("sudo git pull")
	time.sleep(15)

