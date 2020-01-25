import cv2
from PIL import Image
import os
import argparse
from colorama import Fore
from colorama import Style
import time
import glob
from os import system
import uuid


arg = argparse.ArgumentParser()
arg.add_argument("--dir", required=True, help = "Directory of files")
args = vars(arg.parse_args())
ext = ['png', 'jpg', 'jpeg', 'tif']
files = []
[files.extend(glob.glob(args["dir"] + '*.' + e)) for e in ext]
print(Fore.RED+"[+] Inputs"+Style.RESET_ALL)
out = input("Please type a new directory name for the processed images: ")
system("mkdir " + out)
inp = input("Do you want to manually decide the image quality/compression[Y/n]: ")	
if inp == 'Y' or inp == 'y':
	for i in files:
		print("Your current image: " + Fore.RED + i + Style.RESET_ALL)
		img = cv2.imread(i)
		img1 = Image.open(i)
		width, height = img1.size
		copy = width if width > height else height
		lower = (1/(copy/400))*100
		scale_percent = lower
		width = int(img.shape[1] * scale_percent / 100)
		height = int(img.shape[0] * scale_percent / 100)
		dim = (width, height)
		resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		filename = "{}.jpeg".format(uuid.uuid4().hex)
		print("On a scale of 0 to 100, 100 has the best quality and 0 has the least.")
		print("Something less than 90 will be optimum for < 64kB")
		quality = int(input("How much quality do you require: "))
		cv2.imwrite(filename, resized, [cv2.IMWRITE_JPEG_QUALITY, quality])
		system("mv " + filename +" "+ out)
else:
	for i in files:
		print("Dealing with the image: ", i)
		img = cv2.imread(i)
		img1 = Image.open(i)
		width, height = img1.size
		copy = width if width > height else height
		lower = (1/(copy/400))*100
		scale_percent = lower
		width = int(img.shape[1] * scale_percent / 100)
		height = int(img.shape[0] * scale_percent / 100)
		dim = (width, height)
		resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		filename = "{}.jpeg".format(uuid.uuid4().hex)
		cv2.imwrite(filename, resized, [cv2.IMWRITE_JPEG_QUALITY, 85])
		system("mv " + filename +" "+ out)

print(Fore.RED+"[+] done!"+Style.RESET_ALL)