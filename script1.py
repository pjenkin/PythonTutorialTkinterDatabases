from tkinter import *

window = Tk()   # empty window


def km_to_miles():
    # print('Hello')
    print(e1_value.get())
    miles = float(e1_value.get()) * 0.62137
    t1.insert(END, miles)


b1 = Button(window,text="Execute", command=km_to_miles)         # NB no parentheses
# b1.pack()  # simple, button in centre
b1.grid(row=0, column=0, rowspan=2)   # detailed layout, button at top-left and wide (2 columns)


e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)      # text input
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
