import tkinter as tk

root=tk.Tk()

btn=[[0 for x in range(7)]for y in range(7)]
highscoreTable = [["" for x in range (0, 2)]for y in range(0, 10)]

start = tk.Button(root, text = "Start", command = lambda : drawBoard())
start.grid(column=5, row=30, pady=10,padx=10)

with open ("users.txt","r") as f:
            for x in range (10):
                highscoreTable[x][0] = f.readline()
                highscoreTable[x][1] = f.readline()
                nameEntry[x] = tk.Label(text = highscoreTable[x][0][:-1])
                nameEntry[x].grid(column = 7, row = 17+x, padx = 1, pady = 1 )
                scoreEntry[x] = tk.Label(text = highscoreTable[x][1][:-1])
                scoreEntry[x].grid(column = 13, row = 17+x, padx = 1, pady = 1 )
        f.close()

def drawBoard():

    for x in range(7):
        for y in range(7):
            btn[x][y] = tk.Button(root, command = lambda xVar = x, yVar = y :toggle(xVar, yVar))
            btn[x][y].config(text = "1")
            btn[x][y].grid(column=x, row=y)

    btn[3][3].config(text = "0")

    lst_xval=[btn[0][0], btn[0][1],btn[1][0], btn[1][1],
    btn[0][5], btn[0][6],btn[1][5], btn[1][6],
    btn[5][0], btn[5][1],btn[6][0], btn[6][1],
    btn[5][5], btn[5][6],btn[6][5], btn[6][6]]

    for x in range(16):
        lst_xval[x].config(text = "X")

    Wquit = tk.Button(root, text = "Finish", command = lambda: endGame())
    Wquit.grid(column = 6, row = 12)

    start.grid_remove()

    for x in range(10):
        nameEntry[x].grid_remove()
        scoreEntry[x].grid_remove()
def toggle(x, y):

    if x-2 >= 0 and btn[x-2][y].cget("text") == "0" and btn[x-1][y].cget("text") == "1":
        btn[x-2][y].config(text = "M", command = lambda direction = "left": jump(x,y,direction))

    while True:
        try:
            if btn[x+2][y].cget("text") == "0" and btn[x+1][y].cget("text") == "1":
                btn[x+2][y].config(text = "M", command = lambda direction = "right": jump(x,y,direction))
            break
        except IndexError:
            break

    if y-2 >= 0 and btn[x][y-2].cget("text") == "0" and btn[x][y-1].cget("text") == "1":
        btn[x][y-2].config(text = "M", command = lambda direction = "up": jump(x,y,direction))
        

    while True:
        try:
            if btn[x][y+2].cget("text") == "0" and btn[x][y+1].cget("text") == "1":
                btn[x][y+2].config(text = "M", command = lambda direction = "down": jump(x,y,direction))
            break
        except IndexError:
            break

def jump(x, y, direction):

    if direction == "left":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        while True:
            try:
                if btn[x+2][y].cget("text") == "M":
                    btn[x+2][y].config(text = "0", command ="")
                break
            except IndexError:
                break

        while True:
            try:
                if btn[x][y+2].cget("text") == "M":
                    btn[x][y+2].config(text = "0", command ="")
                break
            except IndexError:
                break

        btn[x][y].config(text = "0", command ="")
        btn[x-2][y].config(text = "1", command =lambda xVar= (x-2), yVar = y: toggle(xVar, yVar))
        btn[x-1][y].config(text = "0", command ="")
        
    if direction == "right":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        while True:
            try:
                if btn[x][y+2].cget("text") == "M":
                    btn[x][y+2].config(text = "0", command ="")
                break
            except IndexError:
                break

        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x+2][y].config(text = "1", command =lambda xVar = (x+2), yVar = y: toggle(xVar, yVar))
        btn[x+1][y].config(text = "0", command ="")
		
    if direction == "down":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        while True:
            try:
                if btn[x+2][y].cget("text") == "M":
                    btn[x+2][y].config(text = "0", command ="")
                break
            except IndexError:
                break
        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x][y+2].config(text = "1", command = lambda xVar= x, yVar = (y+2): toggle(xVar, yVar))
        btn[x][y+1].config(text = "0", command ="")
		
    if direction == "up":
        while True:
            try:
                if btn[x][y+2].cget("text") == "M":
                    btn[x][y+2].config(text = "0", command ="")
                break
            except IndexError:
                break

        while True:
            try:
                if btn[x+2][y].cget("text") == "M":
                    btn[x+2][y].config(text = "0", command ="")
                break
            except IndexError:
                break

        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x][y-2].config(text = "1", command =lambda xVar= x, yVar=(y-2): toggle(xVar, yVar))
        btn[x][y-1].config(text = "0", command ="")

def endGame():
    
    score=0
    for x in range(7):
        for y in range(7):
            if btn[x][y].cget("text") == "1":
                score = score + 1

    validate = False

    while validate == False:
        name = simpledialog.askstring("Well Done", "Your score is %s. PLease enter a name to be placed on the leaderboard." % score)
        if name == "":
            messagebox.showerror("Error!", "Please enter a name.")
        else:
            validate = True
    highscoreTable = [["100" for x in range (0, 2)]for y in range(0, 11)]

    highscoreTable[10][0] = name
    highscoreTable[10][1] = score

    with open ("users.txt","r") as f:
        for x in range (10):
            highscoreTable[x][0] = f.readline()
            highscoreTable[x][1] = f.readline()
            highscoreTable[x][0] = highscoreTable[x][0][:-1]
            highscoreTable[x][1] = highscoreTable[x][1][:-1]
            highscoreTable[x][1] = int(highscoreTable[x][1])
    f.close()

    swap = True
    times = len(highscoreTable) - 1

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

    for x in range(11):
        highscoreTable[x][0] = highscoreTable[x][0] +"\n"
        highscoreTable[x][1] = str(highscoreTable[x][1]) + "\n"

    with open ("Users.txt","w") as f:
        for x in range (10):
            f.write(highscoreTable[x][0])
            f.write(highscoreTable[x][1])
    f.close()

    for x in range(7):
        for y in range(7):
            btn[x][y].grid_remove()
    
    Wquit.grid_remove()
    
    start.grid()

    for x in range (10):
            nameEntry[x].grid()
            nameEntry[x].config(text=highscoreTable[x][0])
            scoreEntry[x].grid()
            scoreEntry[x].config(text=highscoreTable[x][1])

    updater = True
root.mainloop()
