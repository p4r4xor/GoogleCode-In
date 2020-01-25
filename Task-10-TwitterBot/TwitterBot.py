#This works on my device, not sure if it works on your device.
#For verification, please visit the handle https://twitter.com/AnikethReddimi
#Password is hidden while you enter

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from getpass import getpass
import time

username = input("Enter your Email Address/ Username/ Phone: ")
password = getpass()

print("[+] Scraping the newest magazine!")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://fedoramagazine.org/")
title = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[1]/div[2]/h2/a")
title_replaced = title.text
link = title.get_attribute("href")
driver.close()
driver.quit()
tweet = "Here is the newest article! \n"+ "Title: "+ title_replaced + "\n" + "Magazine link: " + link
print(tweet)
print("[+] Let's add the link to the twitter handle :)")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://twitter.com/login")
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
element.send_keys(username)
time.sleep(5)
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
element.send_keys(password)
time.sleep(5)
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
element.click()
time.sleep(5)
element = driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[3]/a")
element.click()
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div")
element.send_keys(tweet)
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]")
element.click()
time.sleep(5)
driver.close()
driver.quit()
print("[+] done! Check your handle for more info")
