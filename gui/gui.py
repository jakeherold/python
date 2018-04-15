from tkinter import * 

root = Tk()

# Make frames for window and put them in root window
top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

# Make a button
button1 = Button(top_frame, text="Button 1", fg="red") #Params are (where to put it, what the button says, and what coler it is)
button2 = Button(top_frame, text="Button 2", fg="blue")
button3 = Button(top_frame, text="Button 3", fg="green")
button4 = Button(bottom_frame, text="Button 4", fg="purple")

# Put button in frame.
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()