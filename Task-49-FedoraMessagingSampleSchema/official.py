from fedora_messaging.api import publish, Message
from fedora_messaging.config import conf
from fedora_messaging.api import consume
import sys
done = False
while not done:
	print("[1] Publish Messages")
	print("[2] Listen Messages")
	print("[3] Quit")
	option = int(input("Your option: "))
	if option == 1:
		print("Type 'exit' to quit")
		conf.setup_logging()
		words = []
		while words != "exit":
			words = input("Type your required message: ")
			message = Message(body={"message": words})
			publish(message)
			if words == "exit":
				break
	if option == 2:
		conf.setup_logging()
		consume(lambda message: print(message))

	if option == 3:
		break

