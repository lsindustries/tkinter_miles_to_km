from tkinter import *


window = Tk()
window.title("Miles to KM")
window.minsize(width=200, height=250)
window.config(padx=50, pady=50)

input_miles = Entry(width=20)
input_miles.grid(row=0, column=0)


label = Label(text="Miles is equal to", )
label.grid(row=1, column=0)
label2 = Label(font=("Arial", 22))
label2.grid(row=2, column=0)


def convert():
    miles = input_miles.get()
    km = str((int(miles) * 1.609))+"Km"
    label2.config(text=km)


button = Button(text="Convert", command=convert)
button.grid(row=5, column=0)





















window.mainloop()