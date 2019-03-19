from tkinter import *
import math


def kg_to_imperial():
    kg = float(kg_text_input.get())
    grams = str(kg * 1000) + ' g'
    # pounds = str(kg * 2.20462) + ' lb'
    # ounces = str(kg * 35.274) + ' oz'       # NB not calculating remainder here
    grams_text.insert(END, grams)
    # pounds_text.insert(END, pounds)
    # ounces_text.insert(END, ounces)
    pounds_net = str(round(int(kg * 2.20462), 4)) + ' lb and'
    ounces_net = str(round((math.modf(kg * 2.20462)[0]) * 35.274, 4)) + ' oz'
    pounds_text.insert(END, pounds_net)
    ounces_text.insert(END, ounces_net)

window = Tk()

convert_button = Button(window, text="Convert", command=kg_to_imperial)
convert_button.grid(row=0, column=2)

kg_text_input = Entry(window)
kg_text_input.grid(row=0, column=1)

kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)

grams_text = Entry(window)
grams_text.grid(row=1, column=0)

pounds_text = Entry(window)
pounds_text.grid(row=1, column=1)

ounces_text = Entry(window)
ounces_text.grid(row=1, column=2)


window.mainloop()
