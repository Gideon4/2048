import random
from tkinter import *

root = Tk()

score = 0
hiscore = 0
board = []
squares = []
colors = {0:"#ffffff",2:"#ff9000",4:"#ff0000",8:"#ff0090",16:"#ff00ff",32:"#9000ff",64:"#0000ff",128:"#0090ff",256:"#00ffff",512:"#00ff90",1024:"#00ff00",2048:"#90ff00",4096:"#ffff00"}
sameboard = False

loselabel = Label(root,text = "Score: 0",font = "Arial 24 bold")
loselabel.grid(row = 7,column = 0,columnspan = 4)
scorelabel = Label(root,text = "",font = "Arial 14 bold")
scorelabel.grid(row = 8,column = 0,columnspan = 4)

def newgame():
    global board, score
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    addpiece()
    addpiece()
    score = 0

def restartgame():
    newgame()
    showboard()
    loselabel.config(text="Score: 0")
    scorelabel.config(text="")

def quitnow():
    root.destroy()

def makeboard():
    global squares
    title = Label(root,text = "2048",font = "Arial 24 bold")
    title.grid(row = 0,column = 0,columnspan = 4)
    instructions = Label(root,text = "Use ↑, →, ↓, ← to swipe",font = "Arial 13 bold")
    instructions.grid(row = 1,column = 0,columnspan = 4)
    restart = Button(root,text = "Restart",font = ("Arial 14 bold"),command=restartgame)
    restart.grid(row = 6,column = 0,columnspan = 2)
    quitbutton = Button(root,text = "Quit",font = ("Arial 14 bold"),command = quitnow)
    quitbutton.grid(row = 6,column = 2,columnspan = 2)
    for i in range(4):
        temprow = []
        for j in range(4):
            temprow.append(Label(root,height = 2,width = 4,relief = "ridge",font = "Arial 16 bold"))
        squares.append(temprow)
    for i in range(4):
        for j in range(4):
            squares[i][j].grid(row = i+2,column = j)

def rotate(num):
    global board
    tboard = board.copy()
    for i in range(num):
        boardinprog = []
        for j in range(4):
            temprow = []
            for k in range(4):
                temprow.append(tboard[k][3-j])
            boardinprog.append(temprow)
        tboard = boardinprog.copy()
    board = tboard.copy()
        
def swipe():
    global board,sameboard,score
    tempboard = []
    for i in range(4):
        temprow = board[i].copy()
        tempboard.append(temprow)
    for row in tempboard:
        for i in range(2):
            for j in range(3):
                if row[3-j] == 0:
                    row[3-j] = row[2-j]
                    row[2-j] = 0
        for i in range(3):
            if row[3-i] == row[2-i]:
                row[3-i] *= 2
                score += row[3-i]
                row[2-i] = 0
        for i in range(3):
            if row[3-i] == 0:
                row[3-i] = row[2-i]
                row[2-i] = 0
    sameboard = True
    for i in range(4):
        for j in range(4):
            if tempboard[i][j] != board[i][j]:
                sameboard = False
    board = tempboard.copy()
    loselabel.config(text = "Score: "+str(score))
        
def moveup(e):
    rotate(3)
    swipe()
    rotate(1)
    addpiece()
    showboard()
    checkforloss()

def movedown(e):
    rotate(1)
    swipe()
    rotate(3)
    addpiece()
    showboard()
    checkforloss()

def moveleft(e):
    rotate(2)
    swipe()
    rotate(2)
    addpiece()
    showboard()
    checkforloss()

def moveright(e):
    swipe()
    addpiece()
    showboard()
    checkforloss()

def bindkeys():
    global root
    root.bind("<Up>",moveup)
    root.bind("<Down>",movedown)
    root.bind("<Left>",moveleft)
    root.bind("<Right>",moveright)

def addpiece():
    global sameboard
    if sameboard == False:
        global board
        newrow = random.randint(0,3)
        newcol = random.randint(0,3)
        while board[newrow][newcol] != 0:
            newrow = random.randint(0,3)
            newcol = random.randint(0,3)
        board[newrow][newcol] = 2*(int(random.randint(5,10)/5))
    else:
        sameboard = False


def showboard():
    global squares
    for i in range(4):
        for j in range(4):
            squares[i][j].config(text = board[i][j],bg = colors[board[i][j]])

def checkwin():
    win = False
    for row in board:
        for item in row:
            if item == 2048:
                win = True
    return win

def checkforloss():
    global board
    loss = True
    for row in board:
        for item in row:
            if item == 0:
                loss = False
    for i in range(4):
        for j in range(4):
            try:
                if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]:
                    loss = False
            except:
                pass
    if loss == True:
        loselabel.config(text="You Lose")
        scorelabel.config(text="Your score was "+str(score))

newgame()
makeboard()
showboard()
bindkeys()

root.mainloop()
