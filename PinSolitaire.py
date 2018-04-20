import tkinter as tk

root=tk.Tk()

btn=[[0 for x in range(7)]for y in range(7)]

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

def toggle(x, y):

    if btn[x-2][y].cget("text") == "0" and btn[x-1][y].cget("text") == "1":
        btn[x-2][y].config(text = "M", command = lambda direction = "left": jump(x,y,direction))

    
    if btn[x+2][y].cget("text") == "0" and btn[x+1][y].cget("text") == "1":
        btn[x+2][y].config(text = "M", command = lambda direction = "right": jump(x,y,direction))

    if btn[x][y-2].cget("text") == "0" and btn[x][y-1].cget("text") == "1":
        btn[x][y-2].config(text = "M", command = lambda direction = "up": jump(x,y,direction))

    if btn[x][y+2].cget("text") == "0" and btn[x][y+1].cget("text") == "1":
        btn[x][y+2].config(text = "M", command = lambda direction = "down": jump(x,y,direction))

def jump(x, y, direction):

    if direction == "left":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        if btn[x+2][y].cget("text") == "M":
            btn[x+2][y].config(text = "0", command ="")

        if btn[x][y+2].cget("text") == "M":
            btn[x][y+2].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x-2][y].config(text = "1", command =lambda xVar= (x-2), yVar = y: toggle(xVar, yVar))
        btn[x-1][y].config(text = "0", command ="")
        
    if direction == "right":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        if btn[x][y+2].cget("text") == "M":
            btn[x][y+2].config(text = "0", command ="")

        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x+2][y].config(text = "1", command =lambda xVar = (x+2), yVar = y: toggle(xVar, yVar))
        btn[x+1][y].config(text = "0", command ="")
		
    if direction == "down":
        if btn[x][y-2].cget("text") == "M":
            btn[x][y-2].config(text = "0", command ="")

        if btn[x+2][y].cget("text") == "M":
            btn[x+2][y].config(text = "0", command ="")

        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x][y+2].config(text = "1", command = lambda xVar= x, yVar = (y+2): toggle(xVar, yVar))
        btn[x][y+1].config(text = "0", command ="")
		
    if direction == "up":
        if btn[x][y+2].cget("text") == "M":
            btn[x][y+2].config(text = "0", command ="")

        if btn[x+2][y].cget("text") == "M":
            btn[x+2][y].config(text = "0", command ="")

        if btn[x-2][y].cget("text") == "M":
            btn[x-2][y].config(text = "0", command ="")

        btn[x][y].config(text = "0", command ="")
        btn[x][y-2].config(text = "1", command =lambda xVar= x, yVar=(y-2): toggle(xVar, yVar))
        btn[x][y-1].config(text = "0", command ="")
root.mainloop()
