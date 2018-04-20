import tkinter as tk
from tkinter import messagebox, simpledialog

root=tk.Tk()
root.title("Puck Solitaire")
root.minsize(width=666, height=666)
root.configure(background="#f8f8ff")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(100, weight=1)
root.grid_rowconfigure(100, weight=5)

moving= True
namecount = -1
startFrame = "tk.Frame"
title = "tk.Label"
nameField = "tk.Label"
scoreField = "tk.Label"
start = "tk.Button"
end = "tk.Button"
psHelp = "tk.Button"

nameEntry = [tk.Label for x in range(10)]
scoreEntry = [tk.Label for x in range(10)]

btn=[[0 for x in range(7)]for y in range(7)]

highscoreTable = [[0 for x in range (2)]for y in range(11)]

imageEmpty = tk.PhotoImage(file="Resources\\imageEmpty.gif")
imagemove = tk.PhotoImage(file="Resources\\imagemove.gif")
imagePeg = tk.PhotoImage(file="Resources\\imagePeg.gif")
imageCorner = tk.PhotoImage(file="Resources\\imageBoard.gif")
imageTitle = tk.PhotoImage(file="Resources\\title.gif")
imageTut1 = tk.PhotoImage(file="Resources\\tut1.gif")
imageTut2 = tk.PhotoImage(file="Resources\\tut2.gif")
imageTut3 = tk.PhotoImage(file="Resources\\tut3.gif")

def drawHome():

    global namecount
    global title
    global nameField
    global end
    global scoreField
    global start
    global nameEntry
    global scoreEntry
    global startFrame
    global psHelp

    startFrame = tk.Frame(root, background = "#f8f8ff")
    startFrame.grid(column=10, row = 7)
	
    start = tk.Button(startFrame, background = "#f8f8ff", text = "Start", command = lambda : drawBoard())
    start.grid(column=5, row=30, pady=10,padx=10)

    title = tk.Label(root, background = "#f8f8ff",image = imageTitle)
    title.grid(column=10, row = 5)

    end = tk.Button(startFrame, bg = "#f8f8ff", text = "Exit", command = lambda : quit())
    end.grid(column=15, row = 30, pady=10, padx=10)

    psHelp = tk.Button(startFrame, bg = "#f8f8ff", text = "How To Play", command = lambda : showHelp())
    psHelp.grid(column=5, row = 35, pady=10, padx=10)

    nameField = tk.Label(startFrame, text = "Name", bg = "#f8f8ff")
    nameField.grid(column = 7, row = 15, padx = 10, pady = 20)

    scoreField = tk.Label(startFrame, text = "Score", bg = "#f8f8ff")
    scoreField.grid(column = 13, row = 15, padx = 10, pady = 20)

    namecount= -1

    with open ("Resources\\users.txt","r") as f:
        while True:
            namecount = namecount+1+1
            highscoreTable[namecount][0] = f.readline()
            highscoreTable[namecount][1] = f.readline()
            if highscoreTable[namecount][0][:-1] == "" and highscoreTable[namecount][1][:-1] == "":
                break
            nameEntry[x] = tk.Label(startFrame)
            nameEntry[x].config(bg = "#f8f8ff", text = highscoreTable[namecount][0][:-1])
            nameEntry[x].grid(column = 7, row = 17+x, padx=1, pady=1)
            scoreEntry[x] = tk.Label(startFrame)
            scoreEntry[x].config(bg = "#f8f8ff", text = highscoreTable[namecount][1][:-1])
            scoreEntry[x].grid(column = 13, row = 17+x, padx=3, pady=3)
    f.close()

def drawBoard():
    
    global namecount
    
    for x in range(7):
        for y in range(7):
            btn[x][y] = tk.Button(root, image=imagePeg)
            btn[x][y].config(text = "full", command = lambda xVar = x, yVar = y :toggle(xVar, yVar))
            btn[x][y].grid(column=x+1, row=y+1)

    btn[3][3].config(text = "empty", image = imageEmpty)

    lst_xval=[btn[0][0], btn[0][1],btn[1][0], btn[1][1],
    btn[0][5], btn[0][6],btn[1][5], btn[1][6],
    btn[5][0], btn[5][1],btn[6][0], btn[6][1],
    btn[5][5], btn[5][6],btn[6][5], btn[6][6]]

    for x in range(16):
        lst_xval[x].config(text = "corner", command = '', image = imageCorner)

    title.grid_remove()
    start.grid_remove()
    nameField.grid_remove()
    scoreField.grid_remove()
    end.grid_remove()
    startFrame.grid_remove()

    for x in range(namecount):
        nameEntry[x].grid_remove()
        scoreEntry[x].grid_remove()

def toggle(x, y):

    global moving

    if moving== True:
        if x-2 >= 0 and btn[x-2][y].cget("text") == "empty" and btn[x-1][y].cget("text") == "full":
             btn[x-2][y].config(text = "move", command = lambda direction = "left": jump(x,y,direction), image=imagemove)
             moving = False

        while True:
            try:
                if btn[x+2][y].cget("text") == "empty" and btn[x+1][y].cget("text") == "full":
                    btn[x+2][y].config(text = "move", command = lambda direction = "right": jump(x,y,direction), image=imagemove)
                    moving = False
                break
            except IndexError:
                break

        if y-2 >= 0 and btn[x][y-2].cget("text") == "empty" and btn[x][y-1].cget("text") == "full":
            btn[x][y-2].config(text = "move", command = lambda direction = "up": jump(x,y,direction), image=imagemove)
            moving = False

        while True:
            try:
                if btn[x][y+2].cget("text") == "empty" and btn[x][y+1].cget("text") == "full":
                    btn[x][y+2].config(text = "move", command = lambda direction = "down": jump(x,y,direction), image=imagemove)
                    moving = False
                break
            except IndexError:
                break

def jump(x, y, direction):

    global moving
	
    moving = True

    if direction == "left":
        if btn[x][y-2].cget("text") == "move":
            btn[x][y-2].config(text = "empty", image=imageEmpty, command ="")

        while True:
            try:
                if btn[x+2][y].cget("text") == "move":
                    btn[x+2][y].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break

        while True:
            try:
                if btn[x][y+2].cget("text") == "move":
                    btn[x][y+2].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break

        btn[x][y].config(text = "empty", image=imageEmpty, command ="")
        btn[x-2][y].config(text = "full", command =lambda xVar= (x-2), yVar = y: toggle(xVar, yVar), image=imagePeg)
        btn[x-1][y].config(text = "empty",image=imageEmpty, command ="")
        
    if direction == "right":
        if btn[x][y-2].cget("text") == "move":
            btn[x][y-2].config(text = "empty", image=imageEmpty, command ="")

        while True:
            try:
                if btn[x][y+2].cget("text") == "move":
                    btn[x][y+2].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break

        if btn[x-2][y].cget("text") == "move":
            btn[x-2][y].config(text = "empty", image=imageEmpty, command ="")

        btn[x][y].config(text = "empty", image = imageEmpty, command ="")
        btn[x+2][y].config(text = "full", command =lambda xVar = (x+2), yVar = y: toggle(xVar, yVar), image=imagePeg)
        btn[x+1][y].config(text = "empty", image=imageEmpty, command ="")
		
    if direction == "down":
        if btn[x][y-2].cget("text") == "move":
            btn[x][y-2].config(text = "empty", image=imageEmpty, command ="")

        while True:
            try:
                if btn[x+2][y].cget("text") == "move":
                    btn[x+2][y].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break
        if btn[x-2][y].cget("text") == "move":
            btn[x-2][y].config(text = "empty", image=imageEmpty, command ="")

        btn[x][y].config(text = "empty", image=imageEmpty, command ="")
        btn[x][y+2].config(text = "full", command = lambda xVar= x, yVar = (y+2): toggle(xVar, yVar), image=imagePeg)
        btn[x][y+1].config(text = "empty", image=imageEmpty, command ="")
		
    if direction == "up":
        while True:
            try:
                if btn[x][y+2].cget("text") == "move":
                    btn[x][y+2].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break

        while True:
            try:
                if btn[x+2][y].cget("text") == "move":
                    btn[x+2][y].config(text = "empty", image=imageEmpty, command ="")
                break
            except IndexError:
                break

        if btn[x-2][y].cget("text") == "move":
            btn[x-2][y].config(text = "empty", image=imageEmpty, command ="")

        btn[x][y].config(text = "empty", image=imageEmpty, command ="")
        btn[x][y-2].config(text = "full", command =lambda xVar= x, yVar=(y-2): toggle(xVar, yVar), image=imagePeg)
        btn[x][y-1].config(text = "empty", image=imageEmpty, command ="")
    endcounter = 0
    
    for x in range (7):
        for y in range (7):
            if btn[x][y].cget("text") == "full":
                if y-2 >= 0 and btn[x][y-1].cget("text") == "full" and btn[x][y-2].cget("text") == "empty":
                    endcounter = endcounter + 1
					
                if x-2 >= 0 and btn[x-1][y].cget("text") == "full" and btn[x-2][y].cget("text") == "empty":
                    endcounter = endcounter + 1
					
                while True:
                    try:
                        if btn[x][y+1].cget("text") == "full" and btn[x][y+2].cget("text") == "empty":
                            endcounter = endcounter + 1
							
                        break
						
                    except IndexError:
                        break
						
                while True:
                    try:
                        if btn[x+1][y].cget("text") == "full" and btn[x+2][y].cget("text") == "empty":
                            endcounter = endcounter + 1
							
                        break
						
                    except IndexError:
                        break
                    
    if endcounter == 0:
        endGame()
		
def endGame():

    score=0
    for x in range(7):
        for y in range(7):
            if btn[x][y].cget("text") == "full":
                score = score + 1

    validate = False

    while validate == False:
        name = simpledialog.askstring("Well Done", "Your score is %s. Please enter a name to be placed on the leaderboard." % score)
        name = (name + " ")
	
        if name == " ":
            messagebox.showerror("Error!", "Please enter a name.")
            
        elif len(name) > 16:
            messagebox.showerror("Error!", "Please enter a name less than 17 characters.")
            
        else:
            validate = True

    

    x = -1

    with open ("Resources\\Users.txt","r") as f:
        while True:
            x = x + 1
            highscoreTable[x][0] = f.readline()
            highscoreTable[x][1] = f.readline()
            highscoreTable[x][0] = highscoreTable[x][0][:-1]
            highscoreTable[x][1] = highscoreTable[x][1][:-1]
            if highscoreTable[x][0][:-1] == "" and highscoreTable[x][1][:-1] == "":
                highscoreTable[x][0] = name
                highscoreTable[x][1] = score
                break
            highscoreTable[x][1] = int(highscoreTable[x][1])
    f.close()

    swap = True
    times = len(highscoreTable) -1

    while times > 0 and swap == True:
       swap = False
	   
       for position in range(times):
           if highscoreTable[position][1] > highscoreTable[position + 1][1]:
               swap = True
               temp = highscoreTable[position][1]
               temp2 = highscoreTable[position][0]
               highscoreTable[position][0] = highscoreTable[position + 1][0]
               highscoreTable[position][1] = highscoreTable[position + 1][1]
               highscoreTable[position + 1][1] = temp
               highscoreTable[position + 1][0] = temp2
			   
       times = times - 1

    for x in range(7):
        for y in range(7):
            btn[x][y].grid_remove()

    startFrame.grid()
    title.grid()
    start.grid()
    nameField.grid()
    scoreField.grid()
    end.grid()
	

    for times in range (x):
            nameEntry[times].config(text=highscoreTable[x][0])
            nameEntry[times].grid()
            scoreEntry[times].config(text=highscoreTable[x][1])
            scoreEntry[x].grid()
            highscoreTable[times][0] = highscoreTable[x][0] +"\n"
            highscoreTable[x][1] = str(highscoreTable[x][1]) + "\n"

    with open ("Resources\\Users.txt","w") as f:
        for x in range (x):
            f.write(highscoreTable[x][0])
            f.write(highscoreTable[x][1])
			
    f.close()

def showHelp():

    global help1
    global help2
    global help3
    global Tutu1
    global Tutu2
    global Tutu3
    global back
    
    title.grid_remove()
    start.grid_remove()
    nameField.grid_remove()
    scoreField.grid_remove()
    end.grid_remove()
    startFrame.grid_remove()
    psHelp.grid_remove()

    Tutu1 = tk.Label(image = imageTut1)
    Tutu1.grid(column=5, row=5, pady=10,padx=10)

    help1 = tk.Label(root, background = "#f8f8ff",text = "To make a move, click on a peg with a peg next to it to jump over, and an empty space for the first peg to land in.")
    help1.grid(column=5, row = 10)

    Tutu2 = tk.Label(image = imageTut2)
    Tutu2.grid(column=5, row=15, pady=10,padx=10)

    help2 = tk.Label(root, background = "#f8f8ff",text = "Spaces that are available to be moved into will be highlighted.")
    help2.grid(column=5, row = 20)
    
    Tutu3 = tk.Label(image = imageTut3)
    Tutu3.grid(column=5, row=25, pady=10,padx=10)

    help3 = tk.Label(root, background = "#f8f8ff",text = "Click on a space that is available to be moved into to perform a move.")
    help3.grid(column=5, row = 30)

    back = tk.Button(background = "#f8f8ff", text = "Back", command = lambda : backStart())
    back.grid(column=5, row=35, pady=10,padx=10)

def backStart():
    Tutu1.grid_remove()
    Tutu2.grid_remove()
    Tutu3.grid_remove()
    help1.grid_remove()
    help2.grid_remove()
    help3.grid_remove()
    back.grid_remove()

    title.grid()
    start.grid()
    nameField.grid()
    scoreField.grid()
    end.grid()
    startFrame.grid()
    psHelp.grid()
    
    for x in range (10):
            nameEntry[x].grid()
            scoreEntry[x].grid()

drawHome()

root.mainloop()
