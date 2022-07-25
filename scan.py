#A-70
#https://github.com/A-70/

import time
import os 
from os import system


def sendIp():
	system("clear")
	print("I'm A-70, (full stack developer and cibersecurity expert)")
	Ip = input(str("Ip: "))
	print("ok")
	print("")
	time.sleep(2)
	print("Ping")
	system(f"ping -c 1 {Ip}")
	print("ttl --> 63 Linux, ttl --> 127 windows")
	print("")
	time.sleep(1)
	print("starting nmap...")
	system(f"nmap -n -p- --open -min-rate 5000 T1 -sS -Pn -vvv {Ip} oG ipScan ")
	print("")
	print("finish")	
sendIp()


	
