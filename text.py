import tkinter as tk

window = tk.Tk()

# Create a Text widget with specified width and height
text = tk.Text(window, width=40, height=10)
text.pack()

# Run the Tkinter event loop
window.mainloop()
