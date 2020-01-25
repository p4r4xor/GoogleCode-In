import tkinter as tk
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import requests
from bs4 import BeautifulSoup
import time


def click1():

	browser = Firefox()
	browser.get('https://twitter.com/login')
	login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
	login.send_keys(input("Twitter ID/e-mail address: "))
	paswd = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
	paswd.send_keys(getpass("Twitter Password :"))
	browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
	

def click2():
	browser = Firefox()
	browser.get('https://www.youtube.com/watch?v=vuq-VAiW9kw&list=PL3oW2tjiIxvQ1BZS58qtot3-p-lD32oWT')

def click3():
	driver = Firefox()
	driver.get('https://www.facebook.com/')
	a = driver.find_element_by_id('email')
	a.send_keys(input("Facebook e-mail/phone number: "))
	b = driver.find_element_by_id('pass')
	b.send_keys(getpass("Facebook Password: "))
	driver.find_element_by_id('loginbutton').click()

root = tk.Tk()
root.title("3 tasks")

button1 = tk.Button(root,text="Twitter feed", command=click1, height=2,width=35)
button2 = tk.Button(root,text="Best English playlists 2019", command=click2, height=2,width=35)
button3 = tk.Button(root,text="Facebook feed", command=click3, height=2,width=35)

button1.pack()
button2.pack()
button3.pack()
root.mainloop()