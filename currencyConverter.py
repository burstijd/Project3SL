# Python program to  create a simple GUI
# currency converter using Tkinter

from tkinter import *

# Create a GUI window
window = Tk()

# Window color
window['bg'] = '#85BB65'


# Function to convert currency
# given in dollars to pounds, euros,
# pesos, rubles, yen, and rupees
def from_usd():
    # convert dollar to pound
    pound = float(L2_value.get()) * 0.74

    # convert dollar to peso
    peso = float(L2_value.get()) * 19.77

    # convert dollar to euro
    euro = float(L2_value.get()) * 0.82

    # convert dollar to ruble
    ruble = float(L2_value.get()) * 74.12

    # convert dollar to yen
    yen = float(L2_value.get()) * 104.16

    # convert dollar to yen
    rupee = float(L2_value.get()) * 73.80

    # Enters the converted currency to
    # the text widget
    tw1.delete("1.0", END)
    tw1.insert(END, pound)

    tw2.delete("1.0", END)
    tw2.insert(END, peso)

    tw3.delete("1.0", END)
    tw3.insert(END, euro)

    tw4.delete("1.0", END)
    tw4.insert(END, ruble)

    tw5.delete("1.0", END)
    tw5.insert(END, yen)

    tw6.delete("1.0", END)
    tw6.insert(END, rupee)


# Create the Label widgets
L1 = Label(window, text="Enter your dollar amount")
L2_value = StringVar()
L2 = Entry(window, textvariable=L2_value)
L3 = Label(window, text='Pounds')
L4 = Label(window, text='Pesos')
L5 = Label(window, text='Euros')
L6 = Label(window, text='Rubles')
L7 = Label(window, text='Yen')
L8 = Label(window, text='Rupees')

# Changes colors of the labels and their text
L3.configure(foreground="blue")
L3.configure(background="white")
L4.configure(foreground="green")
L4.configure(background="white")
L5.configure(foreground="black")
L5.configure(background="white")
L6.configure(foreground="yellow")
L6.configure(background="red")
L7.configure(foreground="red")
L7.configure(background="white")
L8.configure(foreground="#BF7E15")
L8.configure(background="white")

# Create the Text Widgets
tw1 = Text(window, height=1, width=20)
tw2 = Text(window, height=1, width=20)
tw3 = Text(window, height=1, width=20)
tw4 = Text(window, height=1, width=20)
tw5 = Text(window, height=1, width=20)
tw6 = Text(window, height=1, width=20)

# Create the Button Widget
b1 = Button(window, text="Convert", command=from_usd)
# Change color of button text
b1.configure(foreground="#1B8C42")

# grid method is used for placing
# the widgets at respective positions
# in table like structure
L1.grid(row=0, column=0)
L2.grid(row=0, column=1)
L3.grid(row=1, column=0)
L4.grid(row=1, column=1)
L5.grid(row=1, column=2)
L6.grid(row=1, column=3)
L7.grid(row=1, column=4)
L8.grid(row=1, column=5)
tw1.grid(row=2, column=0)
tw2.grid(row=2, column=1)
tw3.grid(row=2, column=2)
tw4.grid(row=2, column=3)
tw5.grid(row=2, column=4)
tw6.grid(row=2, column=5)
b1.grid(row=0, column=2)

# Start the GUI
window.mainloop()
