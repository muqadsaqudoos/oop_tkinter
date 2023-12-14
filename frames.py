import tkinter as tk

'''frame = tk.Frame()
frame.pack()
label = tk.Label(master=frame)
#another code
frame_a = tk.Frame()
frame_b = tk.Frame()
label_a = tk.Label(master=frame_a, text="I am in frame A")
label_a.pack()
label_b = tk.Label(master=frame_b, text="I am in frame B")
label_b.pack()
frame_a.pack()
frame_b.pack()

#some code
border_effect= {"flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,}
window = tk.Tk()
for name, value in border_effect.items():
    frame = tk.Frame(master = window, relief = value, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=name)
    label.pack()

#some code
window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.X)

#some code
window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)
'''
#some code
window = tk.Tk()
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)




window.mainloop()