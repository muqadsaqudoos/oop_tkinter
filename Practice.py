#to open gui tkinter module
import tkinter as tk
#window is an intance of Tkinter's tk class and create a new window and assign to the variable window
window = tk.Tk()
#Adding a Widget
'''Now that you have a window, you can add a widget. Use the tk.Label class to add some text to a window.
 Create a Label widget with the text "Hello, Tkinter" and assign it to a variable called greeting:
'''
'''You can control Label text and background colors using the foreground and background parameters'''
'''You can also control the width and height of a label with the width and height parameters:'''
greeting = tk.Label(text= "Hello, Tkinter", fg="black", bg="white", width=10, height=10)

'''The window you created earlier doesn’t change. You just created a Label widget, but you haven’t added 
it to the window yet. There are several ways to add widgets to a window. Right now, you can use the Label 
widget’s .pack() method:'''
greeting.pack()

#Displaying Clickable Buttons With Button Widgets
button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow") 
button.pack()

#Getting User Input With Entry Widgets
entry = tk.Entry(fg="black", bg="white", width=50, command=entry.get())
entry.pack()

window.mainloop()

