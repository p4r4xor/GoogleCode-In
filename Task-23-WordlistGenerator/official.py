from random_word import RandomWords
from itertools import permutations
import sys

def allPermutations(str): 
     permList = permutations(str) 
     for perm in list(permList): 
         print (''.join(perm))
def shouldSwap(string, start, curr):  
  
    for i in range(start, curr):  
        if string[i] == string[curr]:  
            return 0
    return 1 
def findPermutations(string, index, n):  
  
    if index >= n:  
        print(''.join(string))  
        return
  
    for i in range(index, n):   
        check = shouldSwap(string, index, i)  
        if check:  
            string[index], string[i] = string[i], string[index]  
            findPermutations(string, index + 1, n)  
            string[index], string[i] = string[i], string[index] 

r = RandomWords()

words = input("Please enter your required words: ")
string = []
c = 0
while words != "null":
	string.append(words)
	if words.lower() != words:
		string.append(words.lower())
	elif words.upper() != words:
		string.append(words.lower())
	words = input("Please enter your required words: ")
	c = c+1
if c<5:
	print("Not enough inputs. Please run the program again.")
	sys.exit()


dic = []
for i in string:
	dic.append(i)
	for j in range(100):
		dic.append(str(i)+str(j))
		dic.append(str(j)+str(i))
		dic.append(str(i[::-1])+str(j))
		dic.append(str(j)+str(i[::-1]))

for a in range(0, len(string)):
	for b in range(0, len(string)):
		if a!=b:
			dic.append(string[a]+string[b])
			dic.append(string[a]+string[b][::-1])
			dic.append(string[b]+string[a])
			dic.append(string[b]+string[a][::-1])
			for c in range(75):
				dic.append(string[a]+string[b]+str(c))
				dic.append(string[a]+str(c)+string[b])
				dic.append(str(c)+string[a]+string[b])
				dic.append(str(c)+string[a]+string[b][::-1])
				dic.append(str(c)+string[a][::-1]+string[b])
				dic.append(string[a]+str(c)+string[b][::-1])
				dic.append(string[a][::-1]+str(c)+string[b])
				dic.append(string[a]+string[b][::-1]+str(c))
				dic.append(string[a][::-1]+string[b]+str(c))


#for i in dic:
#	dic.append(permutations(i))

final = ""
for i in dic:
    final = final + str(i) + "\n"
file = input("Please enter the name of the file to be saved (new/pre-existing): ")
with open(file,"w+") as f:
    f.write(final)


