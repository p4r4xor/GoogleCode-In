from tkinter import *
from random import choice

class Game():
    def __init__(self, N=4):
        self.field = [[''] * N for i in range(N)]
        self.N = N
        self.add_tile()
        self.add_tile()
  
    def __getitem__(self, index):
        return self.field[index]
    
    def __str__(self):
        return '\n'.join(':'.join(map(str, self[i])) for i in range(self.N))
  
    def left(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N):
                if not self[i][j]: 
                    free += 1
                else:
                    if free > 0:
                        self[i][j - free] = self[i][j]
                        self[i][j] = ''
                        j -= free
                        change = True
                    if j > 0 and self[i][j] == self[i][j - 1]:
                        self[i][j - 1] *= 2
                        self[i][j] = ''
                        change = True                
        if change:          
            self.add_tile()
    
    def right(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N - 1, -1, -1):
                if not self[i][j]: 
                    free += 1
                else:
                    if free > 0:
                        self[i][j + free] = self[i][j]
                        self[i][j] = ''
                        j += free
                        change = True
                    if j < self.N - 1 and self[i][j] == self[i][j + 1]:
                        self[i][j + 1] *= 2
                        self[i][j] = ''
                        change = True                
        if change:          
            self.add_tile()    

    def up(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N):
                if not self[j][i]: 
                    free += 1
                else:
                    if free > 0:
                        self[j - free][i] = self[j][i]
                        self[j][i] = ''
                        j -= free
                        change = True
                    if j > 0 and self[j][i] == self[j - 1][i]:
                        self[j - 1][i] *= 2
                        self[j][i] = ''
                        change = True                
        if change:          
            self.add_tile()    
        
    def down(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N - 1, -1, -1):
                if not self[j][i]: 
                    free += 1
                else:
                    if free > 0:
                        self[j + free][i] = self[j][i]
                        self[j][i] = ''
                        j += free
                        change = True
                    if j < self.N - 1 and self[j][i] == self[j + 1][i]:
                        self[j + 1][i] *= 2
                        self[j][i] = ''
                        change = True                
        if change:          
            self.add_tile()            
    
    def add_tile(self):
        free = [(i, j) for i in range(self.N) 
                for j in range(self.N) if not self[i][j]]
        i, j = choice(free)
        self[i][j] = 2
          
    def game_over(self):
        for line in self.field:
            if '' in line:
                return False
        
        for i in range(self.N):
            for j in range(self.N - 1):
                if self[i][j] == self[i][j + 1]: return False
                if self[j][i] == self[j + 1][i]: return False
        
        return True
N = 4
cell_color = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2"}
color = {'' : '#9e948a', 2 : '#eee4da', 4 : '#ede0c8', 8 : '#f2b179', 16: '#f59563', 32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72', 256: '#edcc61', 512: '#edc850', 1024: '#edc53f', 2048: '#edc22e'}
def left(event):
    game.left()
    draw(game)
    if game.game_over():
        print('GAME OVER')
def right(event):
    game.right()
    draw(game)
    if game.game_over():
        print('GAME OVER')  
def up(event):
    game.up()
    draw(game)
    if game.game_over():
        print('GAME OVER')
def down(event):
    game.down()
    draw(game)
    if game.game_over():
        print('GAME OVER')
def draw(game):
    for i in range(N):
        for j in range(N):
            table[i][j]['text'] = game[i][j]
            try:
                table[i][j]['bg'] = color[game[i][j]]
                table[i][j]['fg'] = cell_color[game[i][j]]
            except KeyError:
                table[i][j]['bg'] = '#9e948a'
root = Tk()
table = [[Label(root, height=2, width=4, font='Arial 36') for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        table[i][j].grid(row=i, column=j)
for i in range(N):
    root.grid_rowconfigure(i, pad=10)
    root.grid_columnconfigure(i, pad=10)
game = Game()
draw(game)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.resizable(False,False)
root.mainloop()