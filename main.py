
########################
#NON LECTURE SOLUTION
#FORMAT IS NOT PRETTY BUT IT WORKS.
from tkinter import *

def button_clicked():
    miles = float(input.get())
    kilometers = miles * 1.609344
    how_many_label.config(text=kilometers)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=75)

#Entry
default_value = IntVar()  #initializes default value to an integer variable
default_value.set(0)        #sets default value to 0
input = Entry(width=10, text=default_value)  #text is now placed to 0 for default value.
print(input.get())
input.grid(row=0, column=1)

#label
mile_label=Label(text="Miles", font=("Arial", 10, "bold"))
mile_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_to_label.grid(row=1, column=0)

how_many_label = Label(text="0")
how_many_label.grid(row=1, column=1)

km_label=Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(row=1, column=2)

#button
button = Button(text="Calculate", command=button_clicked, font=("Arial", 15, "bold"))
button.grid(row=2, column=1)

window.mainloop()
