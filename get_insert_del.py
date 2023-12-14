#Getting User Input With Entry Widgets
'''The interesting bit about Entry widgets isn’t how to style them, though. It’s how to use them to get input from a user.
 There are three main operations that you can perform with Entry widgets:

Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()'''
import tkinter as tk
def get_user_input():
    user_input=entry.get()
    print(user_input)

def del_and_insert():
    entry.delete(0,tk.END)
    entry.insert(0,"Default Text")
window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry(window)
label.pack()
entry.pack()
button = tk.Button(window, command=get_user_input)
button.pack()

button1 = tk.Button(window, text="Clear and Insert Default", command=del_and_insert)
button1.pack()

window.mainloop()

