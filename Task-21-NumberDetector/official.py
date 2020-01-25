import cv2
import os
from PIL import Image
import pytesseract
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("--image", required=True, help = "Image for detection")
args = vars(arg.parse_args())
image = cv2.imread(args["image"])
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, grayscale)
output = pytesseract.image_to_string(Image.open(filename))
number = [int(i) for i in output.split() if i.isdigit()]
print(number)






