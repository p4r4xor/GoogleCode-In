import cv2
import pandas as pd
import argparse
import collections, functools, operator 
import sys
from os import system
import uuid
import time
import glob
from PIL import Image

arg = argparse.ArgumentParser()
arg.add_argument("--img", required=True, help = "Image to be detected")
arg.add_argument("--csv", required=True, help = "Color codes in a CSV")
args = vars(arg.parse_args())
print(args)
img = cv2.imread(args['img'])
cv2.imshow('image',img)
filePath = args['img']
imge = Image.open(filePath)
width, height = imge.size
half = width/2
clicked = False
r=g=b=xpos=ypos= 0
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(args['csv'], names=index, header=None)

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.setMouseCallback('image', click)
done = False
while not done:
    cv2.imshow("image", img)
    num = 10000
    if clicked:
        cv2.rectangle(img, (0, 0), (width, 50), (b, g, r), -1)
        font = cv2.FONT_ITALIC
        for i in range(len(csv)):
            d = abs(r - int(csv.loc[i, "R"])) + abs(g - int(csv.loc[i, "G"])) + abs(b - int(csv.loc[i, "B"]))
            if (d <= num):
                num = d
                cname = csv.loc[i, "color_name"]
        text = cname + ' R='  + str(r) + ' G= ' + str(g) + ' B= ' + str(b)
        textsize = cv2.getTextSize(text, font, 1, cv2.LINE_AA)[0]
        textX = (img.shape[1] - textsize[0]) / 2
        textY = (img.shape[0] + textsize[1]) / 2
        if r + g + b >= 400:
            cv2.putText(img, text, (int(textX), 30),font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, text, (int(textX), 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()