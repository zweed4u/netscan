import os,sys,time,socket
from selenium import webdriver

#Relative and Direct paths stink
driverBin=os.path.expanduser("~/Desktop/chromedriver")
print 'Binary directory:',driverBin

#browser instance
driver=webdriver.Chrome(driverBin)
driver.set_page_load_timeout(5)

socket.setdefaulttimeout(5)
#go to google
i=21
while i <256:
	try:
		driver.get('http://10.0.120.'+str(i))	
	except socket.timeout:
		print 'press escape .',i
	i+=1
	time.sleep(5)
driver.close()
print
