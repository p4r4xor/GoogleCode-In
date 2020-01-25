from spellchecker import SpellChecker
spell = SpellChecker()
print("Please enter the words to be compared in a text file.")
text = input("Please type/paste the paragraph to be checked: ")
words = input("Enter the file name: ")
with open(words, 'r') as wordlist:
	x = [line.rstrip('\n') for line in wordlist]
splitting = text.split()
meow = spell.unknown(splitting)
for i in meow:
	replaced = spell.correction(i)
	if replaced in x:
		position = splitting.index(i)
		splitting.remove(i)
		splitting.insert(position, replaced)
print("Corrected string: " + " ".join([str(i) for i in splitting]))