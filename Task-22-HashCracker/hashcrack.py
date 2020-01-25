import hashlib
import os
import argparse

done = False
#parser = argparse.ArgumentParser()
#parser.add_argument('-d', required=True, help='dictionary file to crack hashes')
#args = vars(parser.parse_args())
#dic = 'rockyou.txt'

dictionary = input("Enter the dictionary name: ")

while not done:
	print("[1] Make Hashes")
	print("[2] Break Hashes")
	print("[3] Quit")
	option = int(input("Enter your option: "))
	if option == 1:
		while not done:
			print("[1] MD5")
			print("[2] SHA1")
			print("[3] SHA224")
			print("[4] SHA256")
			print("[5] SHA384")
			print("[6] SHA512")
			print("[7] Quit")
			hsh = int(input("Enter your option: "))
			if hsh == 1:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.md5(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 2:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.sha1(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 3:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.sha224(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 4:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.sha256(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 5:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.sha384(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 6:
				string = input("Please enter your string to be hashed: ")
				hash_object = hashlib.sha512(string.encode())
				print("Hash for the required string is: ", hash_object.hexdigest())
			elif hsh == 7:
				break
	elif option == 2:
		while not done:
			print("[1] MD5")
			print("[2] SHA1")
			print("[3] SHA224")
			print("[4] SHA256")
			print("[5] SHA384")
			print("[6] SHA512")
			print("[7] Quit")
			hsh = int(input("Enter your option: "))
			if hsh == 1:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.md5(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 2:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.sha1(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 3:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.sha224(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 4:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.sha256(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 5:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.sha384(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 6:
				string = input("Please enter your hash for the chosen option: ")
				cleartext = ''
				with open(dictionary, 'r') as wordlist:
					for line in wordlist:
						x = line.strip('\n')
						meow = hashlib.sha512(x.encode())
						if meow.hexdigest() == string:
							cleartext = line
							break
				if cleartext:
					print("The word is: ",cleartext)
				else:
					print("No match has been found.")
			elif hsh == 7:
				break
	elif option == 3:
		break
	elif option != 1 and \
		 option != 2 and \
		 option != 3:
		print("Not a valid option. Please try again.")







