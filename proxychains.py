#!/usr/bin/python3

import os

title = 'Proxychains Script'
spaces = len(title)

author = 'Finegan'
collab = 'Wre'
date = 'March, 2023'

os.system('clear')

# welcome and credits
def welcome():
	print(title + '\n' + '=' * spaces) 
	print('Author: ' + author)
	print('Collaborator: ' + collab)
	print('Date: ' + date)
	print('-' * spaces + '\n')
	return(welcome)

welcome()
# Select web browser
print('Select your web browser\n'
      '1 = Google Chrome\n' 
      '2 = Firefox (It does not work well)\n'
	  '3 = Chromium\n')
browser = int(input('Choose your web browser: '))

# Install Tor
def installTor():
	print('[+] Installing Tor...')
	os.system('sudo apt install tor')
	return(installTor)

# Install Proxychains
def installProxychains():
	print('[+] Installing Proxychains...')
	os.system('sudo apt install proxychains')
	return(installProxychains)

# Start Tor
def startTor():
	print('[+] Starting Tor...')
	os.system('sudo service tor start')
	return(startTor)

# Start Proxychains Google Chrome
def startProxychainsChrome():
	print('[+] Starting Proxychains on Google Chrome...')
	os.system('proxychains google-chrome google.com')
	return(startProxychainsChrome)

# Start Proxychains Firefox
def startProxychainsFirefox():
	print('[+] Starting Proxychains on Firefox...')
	os.system('proxychains firefox google.com')
	return(startProxychainsFirefox)

# Start Proxychains Chromium
def startProxychainsChromium():
	print('[+] Starting Proxychains on Firefox...')
	os.system('proxychains firefox google.com')
	return(startProxychainsChromium)

def copyConfig():
	print('[+] Copying configuration files...')
	os.system('sudo mv /etc/proxychains.conf /etc/proxychains.conf.bak')
	os.system('sudo mv proxychains.conf /etc/proxychains.conf')
	return(copyConfig)

#Run script
if(os.system('dpkg --get-selections | grep -w proxychains') != 0):
	installProxychains()
elif(os.system('dpkg --get-selections | grep -w tor') != 0):
	installTor()
else:
	os.system('clear')
	welcome()
	copyConfig()
	# Start Tor and Proxychains
	startTor()
	if(browser == 1):
		startProxychainsChrome()
	elif(browser == 2):
		startProxychainsFirefox()
	elif(browser == 3):
		startProxychainsChromium()
	else:
		print('You must choose a web browser')
