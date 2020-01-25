import requests
import argparse
import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent().random
done = False
while not done:
    print("[1] Google")
    print("[2] Bing")
    print("[3] Exit")
    option = int(input("Your option: "))
    if option == 1:
        query = input("Query to be searched: ")
        pages = input("Number of pages: ")
        base_url = "https://www.google.com/search"
        headers  = { "User-Agent": ua }
        params   = { "q": query, "start": pages * 10 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        links  = soup.findAll("cite")
        result = []
        for link in links:
            result.append(link.text)
        print("\n")
        print("Possible vulnerable pages found!")
        print("="*100)
        print(*result, sep = "\n")
        print("="*100)
        counter = 0
        for r in result:
            counter += 1
        print("Total number of URLs: ",counter)
        print("\n")
    if option == 2:
        query = input("Query to be searched: ")
        pages = input("Number of pages: ")
        base_url = "https://www.bing.com/search"
        headers  = { "User-Agent": ua }
        params   = { "q": query, "start": pages * 10 }
        resp = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        links  = soup.findAll("cite")
        result = []
        for link in links:
            result.append(link.text)
        print("\n")
        print("Possible vulnerable pages found!")
        print("="*100)
        print(*result, sep = "\n")
        print("="*100)
        counter = 0
        for r in result:
            counter += 1
        print("Total number of URLs: ",counter)
        print("\n")
    if option == 3:
        break
