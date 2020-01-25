import requests
from bs4 import BeautifulSoup
import argparse
from prettytable import PrettyTable

url = 'https://viewdns.info/reversewhois/?q='
user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

parser = argparse.ArgumentParser(description='Reverse Whois for GCI fedora project')
parser.add_argument("--input", help='Registrant Name or Email Address', required=True)
args = parser.parse_args()

r = requests.get(url + args.input, headers=user_agent)

x = PrettyTable()
x.field_names = ["Domain Name", "Creation Date", "Registrar"]
soup = BeautifulSoup(r.text, 'html.parser')
for row in soup('table')[3].find_all('tr'):
    a = row.find_all('td')[0].text
    b = row.find_all('td')[1].text
    c = row.find_all('td')[2].text
    x.add_row([a,b,c])
    
print(x)






 