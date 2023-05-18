#import tkinter class library.
import tkinter as tk
from tkinter import ttk

#define the event.
def on_select(event):

    #create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#creating the root window.
root = tk.Tk()
root.title("Lord Six")

#creating an array of items.
items = ["item1","Itme 2","Item 3", "Item 4", "Item 5"]

#creating the combo box/placing the combo box inside the root window/populate values.
combo_box = ttk.Combobox(root, values=items)

#The bind funtion will combine the selected item to the on_selected funtion.
combo_box.bind("<<ComboboxSelected>>", on_select)

#pack the object to the root window
combo_box.pack()

#mainloop keeps the root parent window visible.-
root.mainloop()