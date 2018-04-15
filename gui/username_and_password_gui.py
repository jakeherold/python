from tkinter import * 
root = Tk()

# Create Labels and text entry fields, then assign them to a grid in the GUI. 
# Create a checkbox and assign it text
label_user =  Label(root, text="Username")
label_password = Label(root, text = "Password")

entry_user = Entry(root)
entry_password = Entry(root, show="*")

label_user.grid(row=0, sticky=E)
label_password.grid(row=1, sticky=E)

entry_user.grid(row=0, column=1)
entry_password.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me Logged In?")
c.grid(row = 2,columnspan=2)


# Create submit button, declare a print function, and tie the function to it. 
def printName (event):
    print("Your username is:")

submit_button = Button(root, text="Print the thing", command=printName)
submit_button.grid(row=3, columnspan=2)
submit_button.bind('<Button-1>', printName)









root.mainloop()