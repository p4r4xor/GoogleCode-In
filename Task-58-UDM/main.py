from pyexcel_ods import get_data
import json
from pyexcel_ods import save_data
import sys
from os import system
import uuid
import time
import glob
import argparse
import collections, functools, operator 
from prettytable import PrettyTable 
import os.path

def Merge(dict1, dict2, dict3): 
    res = {**dict1, **dict2, **dict3} 
    return res 

arg = argparse.ArgumentParser()
arg.add_argument("--dir", required=True, help = "Directory of files")
args = vars(arg.parse_args())
ext = ['ods']
files = []
data = []
ielts_data = []
interview_data = []
argument = args["dir"]
[files.extend(glob.glob(args["dir"] + '*.' + e)) for e in ext]
print("[+] Given files")
for i in files:
   print(i)
[data.extend(glob.glob(args["dir"] + 'Data?.' + e)) for e in ext]
scores = [sub.replace(argument, '') for sub in data]
[ielts_data.extend(glob.glob(args["dir"] + 'IELT?.' + e)) for e in ext]
ielts = [sub.replace(argument, '') for sub in ielts_data]
[interview_data.extend(glob.glob(args["dir"] + 'Intervie?.' + e)) for e in ext]
interview = [sub.replace(argument, '') for sub in interview_data]
data_result = dict()
ielts_result = dict()
interview_result = dict()
result = dict()

## I didn't hardcode for the Data[i] files as I don't expect them to be only 6 in number :)
tests = [get_data(argument+i)["Sheet1"] for i in scores]
inter = [get_data(argument+i)["Sheet1"] for i in interview]
ielt = [get_data(argument+i)["Sheet1"] for i in ielts]

for row in ielt:
    for coloumn in row[3:]:
        try:
            if coloumn[0] not in ielts_result:
                ielts_result[coloumn[0]] = 0
            numerator = 0
            for inner in range(1,len(coloumn)):
                numerator += coloumn[inner]
            ielts_result[coloumn[0]] += ((((numerator/len(ielt))*100)/36)*3)/10
        except:
            pass
#print(ielts_result)
for row in inter:
    for coloumn in row[3:]:
        try:
            if coloumn[0] not in interview_result:
                interview_result[coloumn[0]] = 0
            numerator = 0
            for inner in range(1,len(coloumn)):
                numerator += coloumn[inner]
            interview_result[coloumn[0]] += ((numerator/len(inter))*6)/10
        except:
            pass
#print(interview_result)
for row in tests:
    for coloumn in row[3:]:
        try:
            if coloumn[0] not in data_result:
                data_result[coloumn[0]] = 0
            numerator = 0
            denominator = 0
            for inner in range(1,len(coloumn)):
                if row[2][inner] == "Geometry" or row[2][inner] == "Algebra" or row[2][inner] == "Physics":
                    numerator += coloumn[inner]*2
                    denominator += 2
                else:
                    numerator += coloumn[inner]
                    denominator += 1
            data_result[coloumn[0]] += (((numerator/denominator)/len(tests))*4)/10
        except:
            pass
#print(data_result)

initial = [data_result, interview_result, ielts_result]
#print(str(initial))
result = dict(functools.reduce(operator.add, 
         map(collections.Counter, initial))) 
#print(str(result))
print("\n")
print("[+] Output")
if os.path.isfile('result.txt'):
    system('rm -rf result.txt')
system('touch result.txt')
x = PrettyTable()
x.field_names = ["Name", "Total score"]
for w in sorted(result, key=result.get, reverse=True):
    a = w
    b = result[w]
    x.add_row([a,b])
print(x)
table = x.get_string()
with open('result.txt', 'w+') as file:
    file.write(table)
