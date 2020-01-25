#!/usr/bin/python3
import requests, argparse, sys, os
from bs4 import BeautifulSoup



sys.path.insert(1 , 'data/')
import ping, crawl

#Import ip
parser = argparse.ArgumentParser(description='Website Crawler')
parser.add_argument('site', type=str, help='Url to Scan')
parser.add_argument('-o', type=str, help='Output File (optional)')
args = parser.parse_args()
site = args.site
file = args.o

def url_handler(site):
    #Handle url
    global site_handled
    site_handled = site
    if "http://" not in site:
        if "https://" not in site:
            site_handled = "https://" + site
    if site_handled[-1:] == "/":
        site_handled = site_handled[:-1]
        return site_handled


url_handler(site)
ping.ping(site_handled)

#get site contents
website_url = requests.get(site_handled)
soup = BeautifulSoup(website_url.content,'html.parser',from_encoding="iso-8859-1")

crawl.cr(soup, website_url, site_handled, file)
