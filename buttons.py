from tkinter import  *


class Buttons:
    def buttons_amount(self, master, linha):
        Button(master, width=10, height=1, text="-").grid(row=linha, column=1)
        Entry(master, font=("arial", 18, "bold"), state=DISABLED, width=3).grid(row=linha, column=2)
        Button(master, width=10, height=1, text="+").grid(row=linha, column=3)

    def raised_button(self, master, var, title,linha, color_button="black"):
        Checkbutton(master, text=title, variable=var, onvalue=1, offvalue=0, bg=color_button, bd=1,
                            font=("arial", 18, "bold")).grid(row=linha, sticky=W)