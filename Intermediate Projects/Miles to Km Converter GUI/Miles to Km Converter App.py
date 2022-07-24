from tkinter import *

# Create window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=150)

# *****TOP HALF
# Create the entry box that will store the miles value
miles_entry = Entry(width=8, font=("Rosewood Std Regular", 14, "normal"))
miles_entry.grid(row=2, column=2)

# Create "Miles" label
miles_label = Label(text='Miles', font=("Rosewood Std Regular", 14, "normal"))
miles_label.grid(row=2, column=3)
miles_label.config(padx=10)

# *****BOTTOM HALF
# Create empty label object to set up initial grid position
empty_label = Label(text='')
empty_label.grid(row=0, column=0)
empty_label.config(padx=70, pady=10)

# Create "is equal to" label
equal_to_label = Label(text='is equal to', font=("Rosewood Std Regular", 14, "normal"))
equal_to_label.grid(row=3, column=0)

# Create the conversion Label
conversion_label = Label(text='', font=("Rosewood Std Regular", 14, "normal"))
conversion_label.grid(row=3, column=2)

# Create 'Km' Label
km_label = Label(text='Km', font=("Rosewood Std Regular", 14, "normal"))
km_label.grid(row=3, column=3)


# Create 'Calculate' button
def calculate():
    user_miles = int(miles_entry.get())
    user_km = round(user_miles * 1.609344)
    conversion_label.config(text=user_km)


calculate_button = Button(text='Calculate', font=("Rosewood Std Regular", 10, "bold"), command=calculate)
calculate_button.grid(row=4, column=2)
calculate_button.config(pady=3)

# Function to keep window open and listen for key-presses
window.mainloop()
