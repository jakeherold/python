from tkinter import * 

root = Tk()

one = Label(root, text="One", bg='black', fg='yellow')
one.pack()
two = Label(root, text="Two", bg='white', fg='black')
two.pack(fill=X) # "fill=x" means that the button should flex with the horizontal sides size
three = Label(root, text="three", bg='white', fg='black')
three.pack(side=LEFT, fill=Y) # "fill=y" means that the button should flex with the vertical side's size

root.mainloop()