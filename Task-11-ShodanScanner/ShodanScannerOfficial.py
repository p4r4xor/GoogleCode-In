import scapy.all as scapy
import argparse
import requests, argparse, sys, os
from bs4 import BeautifulSoup
import shodan
from prettytable import PrettyTable

print("Please login/register at https://account.shodan.io/login for generation of an API key")
print("Go to https://account.shodan.io/ to view your API key")
done = False
while not done:

	api_key = str(input("Enter your API key: "))
	if(len(api_key) != 32):
		print("This isn't a valid key. Try again.")
	else:
		break

api =  shodan.Shodan(api_key)

while not done:
	print("You have 4 options: ")
	print("[1] Get your IP")
	print("[2] Scanning a specific Host")
	print("[3] Shodan Search to scan IPs, Hostnames, ports")
	print("[4] Quit")
	option = int(input("Enter your option: "))
	if option == 1:
		ip = api.tools.myip()
		print(ip)
	elif option == 2:
		host_ip = input("Input a IP address for scanning: ")
		scan = api.host(host_ip, history=True)
		print("Hostname: ", " "*9, scan['hostnames'])
		print("City: ", " "*13, scan["city"])
		print("Country: ", " "*10, scan["country_name"])
		print("Organization: ", " "*5, scan["org"])
		print("Operating System: ", " "*1, scan["os"])
		print("Latitude: ", " "*9, scan["latitude"])
		print("Longitude: "," "*8, scan["longitude"])
		print("Port: ", " "*13, scan["data"][0]["port"])
	elif option ==3:
		search = input("Query to be searched: ")
		scan = api.search(search)
		x = PrettyTable()
		x.field_names = ["IP", "Port", "Organization"]
		for i in scan['matches']:
			a = i['ip_str']
			b = i['port']
			c = i['org']
			x.add_row([a,b,c])
		print(x)
	elif option == 4:
		break
		
