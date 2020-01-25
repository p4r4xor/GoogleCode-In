import requests as req
websites = [
	"https://www.github.com/",
	"https://www.instagram.com/",
	"https://www.twitter.com/"
]
useragent = {'useragent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
username = input("Username: ")
for i in websites:
	response = req.get(i + username, headers=useragent)
	if response.status_code == 200:
		p = i.replace('https://www.', '')
		print("Found in " + p.replace('.com/', ''))


