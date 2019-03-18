from tkinter import *

window = Tk()   # empty window

b1 = Button(window,text="Execute")
# b1.pack()  # simple, button in centre
b1.grid(row=0, column=0, rowspan=2)   # detailed layout, button at top-left and wide (2 columns)

e1 = Entry(window)      # text input
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width = 20)
t1.grid(row=0, column=2)

window.mainloop()
