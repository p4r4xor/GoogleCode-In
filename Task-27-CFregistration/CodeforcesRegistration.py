from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from getpass import getpass
import time
import sys

username = input("Enter your Handle/Email: ")
password = getpass()

print("[+] Logging you into your account!")

driver = Firefox()
driver.get("https://codeforces.com/enter")
element = driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
element.send_keys(username)
element = driver.find_element_by_xpath('//*[@id="password"]')
element.send_keys(password)
element = driver.find_element_by_xpath('//*[@class="submit"]')
element.click()

print("[+] Opening contests page!")

driver.get("http://codeforces.com/contests")
x = []
allcontests = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr')[1:]
for i,j in zip(range(2), allcontests):
	try:
		y = j.find_element_by_xpath('//*[@class="red-link"]').get_attribute('href')
		x.append(y)
	except NoSuchElementException:
		pass
for i,y in enumerate(x):
	driver.get(y)
	driver.save_screenshot(f'registration{i}.png')
	last = driver.find_element_by_xpath('//*[@class="submit"]')
	last.location_once_scrolled_into_view
	last.click()
	driver.save_screenshot(f'registration_done{i}.png')

print("[+] Done!")
driver.quit()


