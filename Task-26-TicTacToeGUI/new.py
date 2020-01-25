from tkinter import *
from tkinter import Button
from tkinter import messagebox
from random import choice
from tkinter import (N,S,W,E)

root=Tk()
root.title("TicTacToe GUI")

bclick=choice([False,True])


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

def restartbutton():
    b1['text']=' '
    b2['text']=' '
    b3['text']=' '
    b4['text']=' '
    b5['text']=' '
    b6['text']=' '
    b7['text']=' '
    b8['text']=' '
    b9['text']=' '
    if b1["state"] == DISABLED:
        b1["state"] = NORMAL
    if b2["state"] == DISABLED:
        b2["state"] = NORMAL
    if b3["state"] == DISABLED:
        b3["state"] = NORMAL
    if b4["state"] == DISABLED:
        b4["state"] = NORMAL
    if b5["state"] == DISABLED:
        b5["state"] = NORMAL
    if b6["state"] == DISABLED:
        b6["state"] = NORMAL
    if b7["state"] == DISABLED:
        b7["state"] = NORMAL
    if b8["state"] == DISABLED:
        b8["state"] = NORMAL
    if b9["state"] == DISABLED:
        b9["state"] = NORMAL
    

def disableButton():
    if b1["state"] == NORMAL:
        b1["state"] = DISABLED
    
    if b2["state"] == NORMAL:
        b2["state"] = DISABLED
    
    if b3["state"] == NORMAL:
        b3["state"] = DISABLED
    
    if b4["state"] == NORMAL:
        b4["state"] = DISABLED
    
    if b5["state"] == NORMAL:
        b5["state"] = DISABLED
    
    if b6["state"] == NORMAL:
        b6["state"] = DISABLED
    
    if b7["state"] == NORMAL:
        b7["state"] = DISABLED
    
    if b8["state"] == NORMAL:
        b8["state"] = DISABLED
    
    if b9["state"] == NORMAL:
        b9["state"] = DISABLED
    
    
def messageWindow():
    win = Toplevel()
    win.title('warning')
    message = "This will delete stuff"
    Label(win, text=message).grid()
    Button(win, text='Delete', command=win.destroy).grid()

def tictactoe(buttons):
    global bclick
    if buttons["text"]==" " and bclick == True:
        buttons["text"]="X"
        bclick=False
    elif buttons["text"]==" " and bclick == False:
        buttons["text"]="O"
        bclick=True
    if (  b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X" or b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        #Button(root, text='Bring up Message', command=messageWindow).grid()
        disableButton()
        messagebox.showinfo("Game Over","Player X won the game!")
        
        #root.destroy()
    elif (  b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O" or b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
        #Button(root, text='Bring up Message', command=messageWindow).grid()
        disableButton()
        messagebox.showinfo("Game Over","Player O won the game!")
        
        #root.destroy()
    elif (b1["text"]!=" " and b2["text"]!=" " and b3["text"]!=" " and b4["text"]!=" " and b5["text"]!=" " and b6["text"]!=" " and b7["text"]!=" " and b8["text"]!=" " and b9["text"]!=" "):
        #Button(root, text='Bring up Message', command=messageWindow).grid()
        disableButton()
        messagebox.showinfo("Game Over","It is Draw!")
        
        #root.destroy()
        
reset=HoverButton(root,text="New Game",height=2,width=35,command=lambda:restartbutton(),bg="#eee4da",fg="#776e65",activebackground='#ede0c8',activeforeground='#776e65')

b1=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b1),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b2=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b2),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b3=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b3),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b4=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b4),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b5=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b5),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b6=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b6),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b7=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b7),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b8=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b8),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')
b9=HoverButton(root,text=" ",font='Arial 24',height=2,width=4,command=lambda:tictactoe(b9),bg="#f2b179",fg="#f9f6f2",activebackground='#ede0c8',activeforeground='#776e65')

reset.grid(row=1,column=1,columnspan=3,sticky=W+E)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
b4.grid(row=3,column=1)
b5.grid(row=3,column=2)
b6.grid(row=3,column=3)
b7.grid(row=4,column=1)
b8.grid(row=4,column=2)
b9.grid(row=4,column=3)


root.resizable(False,False)
root.mainloop()