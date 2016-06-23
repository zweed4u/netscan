#!/bin/bash

NET=0 #120
while [ $NET -lt 125 ]; do	
	sudo nmap -sP --max-retries=3 --host-timeout=5000ms 10.0.$NET.0/24
	echo nmap -sP report for 10.0.$NET.0/24 above. 
	let NET=NET+1 
done
