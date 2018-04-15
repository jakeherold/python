from tkinter import * 

root = Tk()


label_user =  Label(root, text="Username")
label_password = Label(root, text = "Password")
entry_user = Entry(root)
entry_password = Entry(root)

label_user.grid(row=0)
label_password.grid(row=1)

entry_user.grid(row=0, column=1)
entry_password.grid(row=1,column=1)


root.mainloop()