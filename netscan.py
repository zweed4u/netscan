import os,sys,time,socket
from selenium import webdriver

#Relative and Direct paths stink
driverBin=os.path.expanduser("~/Desktop/chromedriver")
print 'Binary directory:',driverBin

#browser instance
driver=webdriver.Chrome(driverBin)
driver.set_page_load_timeout(5)

socket.setdefaulttimeout(5)
#Class A
lastOctet=0
thirdOctet=120
while thirdOctet<124:
	while lastOctet <256:
		try:
			driver.get('http://10.0.'+str(thirdOctet)+'.'+str(lastOctet))	
		except socket.timeout:
			print 'press escape 10.0.'+str(thirdOctet)+'.'+str(lastOctet)
		lastOctet+=1
		time.sleep(5)
	lastOctet=0
	thirdOctet+=1
driver.close()
print 'Scan Complete'