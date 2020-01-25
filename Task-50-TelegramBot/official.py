from telegram.ext import Updater ,CommandHandler
import telegram
import json
import os
import requests
from prettytable import PrettyTable

token="API key here"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def forks(update,context):
    repos=requests.get("https://api.github.com/orgs/fedora-infra/repos").json()
    #print(repos)
    x = PrettyTable()
    x.field_names = ["Repo Name", "Forks count"]
    output=str()
    for i in repos:
        a = i["name"]
        b = str(i["forks_count"])
        x.add_row([a,b])
        output+=(" [+] Repository: "+i["name"]+"\n"+"       Number of forks: "+str(i["forks_count"])+"\n")
        #print(i["name"])
    update.message.reply_text(output)

def individual(update,context):
    repos=requests.get("https://api.github.com/orgs/fedora-infra/repos").json()
    output = str()
    for i in repos:
        if i["name"] in context.args:
            output += (" [+] Repository: "+i["name"]+"\n"+"       Number of forks: "+str(i["forks_count"])+"\n")
    update.message.reply_text(output)

dispatcher.add_handler(CommandHandler("forks", forks))
dispatcher.add_handler(CommandHandler("individual", individual))
updater.start_polling()
updater.idle()
