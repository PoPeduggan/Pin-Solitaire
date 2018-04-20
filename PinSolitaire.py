import tkinter as tk

root=tk.Tk()

btn=[[0 for x in range(7)]for y in range(7)]

for x in range(7):
    for y in range(7):
        btn[x][y] = tk.Button(root)
        btn[x][y].config(text = "1")
        btn[x][y].grid(column=x, row=y)

root.mainloop()