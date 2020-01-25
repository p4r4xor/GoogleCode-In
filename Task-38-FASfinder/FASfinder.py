from fedora.client.fas2 import AccountSystem
account = AccountSystem(username='paraxor', password='XXX')
user_search = input("Please enter the required username to be searched: ")
user = (str(account.people_by_key(key=u'username',search=user_search,fields=['email'])))[34:-4]
print("Email found: ", user)
