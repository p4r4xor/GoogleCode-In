import sys
import os
from os import system
import optparse
import pyshark
import operator
import hexdump
import nest_asyncio
from prettytable import PrettyTable 

nest_asyncio.apply()
def connection():
    print("This will take a while")
    capture = pyshark.FileCapture(filedir)
    ide={'1':'ICMP','4':'IPv4','6':'TCP','17':'UDP','41':'IPv6',}
    x = PrettyTable()
    x.field_names = ["Protocol", "Source IP", "Source port", "Dest IP", "Dest port"]
    for i in capture:
        try:
            proto=ide[i['ip'].proto]
            a = proto
            b = i['ip'].src
            c = i[proto].srcport
            d = i['ip'].dst
            e = i[proto].dstport
            x.add_row([a,b,c,d,e])
        except:
            pass
    print(x)

def ip():
    print("This will take a while")
    capture = pyshark.FileCapture(filedir)
    record=dict()
    for i in capture:
        try:
            a,b=i['ip'].src,i['ip'].dst
            try:
                record[a]+=1
            except:
                record[a]=1
            try:
                record[b]+=1
            except:
                record[b]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    x = PrettyTable()
    x.field_names = ["count", "IP"]
    for i in range(len(record)):
        a = record[i][1]
        b = record[i][0]
        x.add_row([a,b])
    print(x)

def ports():
    print("This will take a while")
    capture = pyshark.FileCapture(filedir)
    record=dict()
    for i in capture:
        try:
            ide={'1':'ICMP','6':'TCP','17':'UDP'}
            proto=ide[i['ip'].proto]
            a,b=i[proto].srcport,i[proto].dstport
            try:
                record[a]+=1
            except:
                record[a]=1
            try:
                record[b]+=1
            except:
                record[b]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    x = PrettyTable()
    x.field_names = ["count", "IP"]
    for i in range(len(record)):
        a = record[i][1]
        b = record[i][0]
        x.add_row([a,b])
    print(x)

parser = optparse.OptionParser('usage: %s --file' % sys.argv[0])
parser.add_option('--file', dest='filedir', type='string', help='pcap file to be analyzed')
options,argvs = parser.parse_args()
if(options.filedir==None):
	print(parser.usage)
	sys.exit(0)
elif(options.filedir!=None):
	filedir = options.filedir
	print("Given file for analysis: ", filedir)
	done = False
	while not done:
		print("[1] Top 10 visited sites")
		print("[2] Useragents")
		print("[3] Connection details")
		print("[4] List of IPs")
		print("[5] List of ports")
		print("[6] Grep mode")
		print("[7] Quit")
		inp = int(input("Enter your option: "))
		if inp == 1:
			system("sudo tshark -e http.host -T fields -r "+filedir+" | sort | uniq -c | sort -nr | head")
		if inp == 2:
			system('sudo tshark -r '+filedir+' -Y \'http contains "User-Agent:"\' -T fields -e http.user_agent | sort | uniq -c | sort -nr')
		if inp == 3:
			connection()
		if inp == 4:
			ip()
		if inp == 5:
			ports()
		if inp == 6:
			string = input("Word to be searched: ")
			system('sudo tcpdump -r '+filedir+' -A | grep "'+string+'"')
		if inp == 7:
			break



			
			










