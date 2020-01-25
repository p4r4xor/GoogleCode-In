import scapy.all as scapy
import argparse
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]
    clients = []
    for e in answered:
        client_dict = {"ip": e[1].psrc, "mac": e[1].hwsrc}
        clients.append(client_dict)
    return clients
def printscan(clients):
    print("                                        ")
    print("    IP\t\t|    MAC Address")
    for e in clients:
        print(e["ip"]+" \t| "+  e["mac"])
    print("\n")
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", dest="ip", help=" specify the IP Address")
    options = parser.parse_args()
    if not options.ip:
        parser.error("consider adding --help to the command line.")
    return options
try:
    printscan(scan(get_arguments().ip))
except KeyboardInterrupt:
    print("\n [-] KeyboardInterrupt ")



