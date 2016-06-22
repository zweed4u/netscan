I was given the task of finding/upgrading a company KVM Switch's firmware. With no prior experience I researched and sought an answer online. I stumbled across some manuals and other somewhat useful materials. But it wasn't long until I hit a road block. After fumbling with the hardware, I began to prepare for the upgrade, downloading necessary files. But I could advance no further when I was prompted to login into the KVM switch via it's ip address. I had the Mac address supplied but I couldn't get the ip address due to the inability to log into the network router. I tried various arp, nstat, and nmap commands.

For some reason I was still unable to see the device on the network. Ignoring the fact that the device could have in fact, have no interface up/ip associated it with it, I took to what I know.

I tried to find a way to automate a network scan/sweep. I first recalled a script I developed a while back I used for scraping. It was a bundled javascript and json file for a chrome extension crx file. Using window.location.href, some string manipulation and settimeout a pseudo crawler can easily be created. The problem with this is that the declaration of variables is deterimental to functionality becuase of the script's reinitialization per page reload. This is a nuisance.

Python is my bread and butter. I quickly turned to IDLE to try some few ideas. I first thought of using the requests module but due to the nature of visiting ip addresses, some result in unreachable hosts and therefore contents are inaccessible. I thought of a better way, why not turn to selenium? I would still need to keep a watchful eye on run time but it would automate most of the human element in the process. I downloaded the chrome binary for my webdriver and off I went.  

Unfortunately, in hindsight, the ip address returned a 'requested url was not found'. Upon looking further into the documentation, I would find that my scripts wouldn't do the trick. Instead I needed an appended '/config'. Rather than adjust my script in fear of time constraints, I found that I had been giving incorrect arguments to the nmap command. First running ifconfig to find the correct network to scan I found the inet addr:10.0.120.X. I used this for my sweep.

sudo nmap -sP 10.0.120.0/24

It took a second to get the formatting but with a copy and paste to a text editor, I was able to cntl+f the mac address and found the nmap report for the device.
