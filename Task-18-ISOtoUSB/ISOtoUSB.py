from os import system
import subprocess
import time
import sys
import requests
from bs4 import BeautifulSoup
import wget

def get_choice():
    choice = input("Your choice: ")
    return choice
def clrscr():
    os.system('clear')    
def take_input(List):
    for i, elem in enumerate(List):
        print(f'{i+1}: {elem}')
    choice = get_choice()
    assert choice.isdigit() and int(choice) in range(1, len(List)+1)
    return List[int(choice)-1]
class Checksum:
    def verify(self, checksum_file, fedora_version):
        with open(checksum_file) as f:
            data = f.readlines()
        hash_name = data[1].split(': ')[1].lower()
        index = None 
        for i in range(2, len(data)):
            data[i] = data[i].strip('\n')
            if fedora_version in data[i]:
                index = i+1
                break 
        if not index:
            print('Couldn\'t find checksum of the give iso file')
        checksum = data[index].split(' = ')[1].strip('\n')
        output = sp.check_output([f'echo "{checksum} *{fedora_version}" | shasum -a 256 --check'], shell=True)
        if output.decode('utf8').split(': ')[1].strip('\n') == 'OK':
            return True
        return False
class downloadISO:
    def download(self):
        self.pprint(lambda: print("Getting Latest Fedora Version."))
        base_url = "https://dl.fedoraproject.org/pub/fedora/linux/releases"
        soup = self.get_soup(base_url)
        Links = self.get_links(soup)
        Versions = []
        for link in Links:
            link = link.text.strip('/')
            if link.isdigit():
                Versions.append(int(link))
        print(f'The latest version is {max(Versions)}')
        choice = take_input(['Workstation', 'Spins'])
        base_url += f'/{max(Versions)}/{choice}/x86_64/iso'
        soup = self.get_soup(base_url)
        Links = self.get_links(soup)
        ISOs = [link.text for link in Links if '.iso' in link.get('href')]
        CHECKSUM = None
        for link in Links:
            if 'CHECKSUM' in link.text:
                CHECKSUM = link.text 
        self.pprint(lambda: print('The available ISOs: '))
        choice = take_input(ISOs)
        if not CHECKSUM:
            print('No checksum found, do you still want to proceed?')
            choice = take_input(['Yes.', 'No.'])
            if choice == 2:
                exit()
        wget.download(base_url+'/'+choice, choice)
        if CHECKSUM:
            print('Downloading checksum')
            wget.download(CHECKSUM, 'checksum')
            CHECKSUM = 'checksum.txt'
        return CHECKSUM, choice 
    def pprint(self, func):
        func()
    def get_links(self, soup):
        return soup.findAll('a')
    def get_soup(self, url):
        return BeautifulSoup(requests.get(url).content, "lxml")
def main():
    downloadISO().download()
    print(Checksum().verify('checksum', 'Fedora-Workstation-Live-x86_64-31-1.9.iso'))
if __name__ == "__main__":
    main()
print("Use this at your own risk.")
print("Copy your required ISO file into the current directory before moving forward.")
input("Please insert your USB flash drive and hit Enter")
system("lsblk")
usb = input("Enter the alphabet of your USB flash drive. (e.g. '/dev/sda' == 'a' or '/dev/sdc' == 'c'): ")
No = input("You hence agree to wipe your current USB flash drive. Continue[Y/n] ")
if No == 'n':
	quit()
print("The following process might take time, please be patient.")
system("sudo shred -fvzn0 /dev/sd%s" % usb)
print("Done!")
x = input("You hence agree to burn your disk image to your current USB flash drive. Continue[Y/n] ")
if x == 'n':
	quit()
iso = input("Enter the name of the required ISO file: ")
system("dd bs=4M if=%s of=/dev/sd%s" % (iso,usb))
print("Done! Your required ISO file is now burnt/cloned to the USB flash drive.")
