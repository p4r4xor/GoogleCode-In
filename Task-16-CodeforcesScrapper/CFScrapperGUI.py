import tkinter as tk
from datetime import datetime
from urllib.request import urlopen
import json
import numpy as np

def getInformation(handle):
    handle = filterHandle(handle)
    if len(handle) > 24 or len(handle) < 3:
        raise InvalidLengthException()
    url = "https://codeforces.com/api/user.info?handles=" + handle
    with urlopen(url) as req:
        result = json.load(req)
    assert result["status"] == "OK"
    result = result["result"][0]
    return {
            "rating": result["rating"],
            "maxRating": result["maxRating"],
            "rank": result["rank"],
            "maxRank": result["maxRank"],
            "registrationTime": result["registrationTimeSeconds"]
           }

def RatingData(handle, startTime):
    handle = filterHandle(handle)
    url = "https://codeforces.com/api/user.rating?handle=" + handle
    with urlopen(url) as req:
        result = json.load(req)
    assert result["status"] == "OK"
    result = result["result"]
    result = [(datetime.fromtimestamp(startTime), 1500)] \
        + [(datetime.fromtimestamp(entry["ratingUpdateTimeSeconds"]), entry["newRating"]) for entry in result]
    return np.transpose(result)

def Color(rank):
    if "grandmaster" in rank: 
        return "red"
    elif "candidate master" in rank: 
        return "violet"
    elif "master" in rank: 
        return "orange"
    elif "expert" in rank: 
        return "blue"
    elif "specialist" in rank: 
        return "cyan"
    elif "pupil" in rank: 
        return "green"
    else: 
        return "gray"

def filterHandle(handle):
    handle_result = "".join(filter(lambda c: c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-", handle))
    return handle_result

class CF(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.namevar = tk.StringVar()
        self.username = tk.Entry(self, width=15, textvariable=self.namevar)
        self.username.grid(row=0,column=1)
        tk.Label(self, text="Username: ").grid(row=0, column=0)
        self.submit_button = tk.Button(self, text="submit", command=self.get_info)
        self.submit_button.grid(row=0, column=2)
        self.result_box = tk.Text(self, width=50, height=10, state=tk.DISABLED)
        self.result_box.grid(row=1, column=0, columnspan=4)
        self.result_box.tag_config("red", foreground="#ff0000")
        self.result_box.tag_config("gray", foreground="#808080")
        self.result_box.tag_config("violet", foreground="#a0a")
        self.result_box.tag_config("orange", foreground="#ff8c00")
        self.result_box.tag_config("blue", foreground="#0000ff")
        self.result_box.tag_config("cyan", foreground="#03a89e")
        self.result_box.tag_config("green", foreground="#008000")
        
        self.info = {}
    
    def get_info(self):
        info = getInformation(self.namevar.get())
        info["name"] = self.namevar.get()
        rank = info["rank"]
        rating = info["rating"]
        maxRank = info["maxRank"]
        maxRating = info["maxRating"]
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.INSERT, "Name: ")
        self.result_box.insert(tk.INSERT, filterHandle(self.namevar.get()))
        self.result_box.insert(tk.INSERT, "\n\nRating: ")
        self.result_box.insert(tk.INSERT, str(rating), Color(rank))
        self.result_box.insert(tk.INSERT, "\n\nRank: ")
        self.result_box.insert(tk.INSERT, rank, Color(rank))
        self.result_box.insert(tk.INSERT, "\n\nMax Rating: ")
        self.result_box.insert(tk.INSERT, maxRating, Color(maxRank))
        self.result_box.insert(tk.INSERT, "\n\nMax Rank: ")
        self.result_box.insert(tk.INSERT, maxRank, Color(maxRank))
        self.result = info

cfgui = tk.Tk()
gui = CF(cfgui)
cfgui.mainloop()
