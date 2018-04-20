import tkinter as tk

root=tk.Tk()

btn=[[0 for x in range(7)]for y in range(7)]

for x in range(7):
    for y in range(7):
        btn[x][y] = tk.Button(root)
        btn[x][y].config(text = "1")
        btn[x][y].grid(column=x, row=y)

btn[3][3].config(text = "0")

lst_xval=[btn[0][0], btn[0][1],btn[1][0], btn[1][1],
btn[0][5], btn[0][6],btn[1][5], btn[1][6],
btn[5][0], btn[5][1],btn[6][0], btn[6][1],
btn[5][5], btn[5][6],btn[6][5], btn[6][6]]

for x in range(16):
    lst_xval[x].config(text = "X")

root.mainloop()
