import tkinter as tk
root = tk.Tk()
root.geometry("500x300")
root.title("My First GUI")
label = tk.Label(root, text="Registration form", font=("Arial",18))
label.pack(padx = 10, pady = 10)
name = tk.Label(root, text="Name")
name.pack()
phone = tk.Label(root, text="Phone")
phone.pack()
gender = tk.Label(root, text="Gender")
gender.pack()



root.mainloop()
