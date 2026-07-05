from tkinter import *

def vasooli():
    broot=Toplevel()
    broot.geometry("1920x1080")
    broot.title("transaction history")
    broot.config(bg="#121212")
    label=Label(broot,text="Here's is your transaction history",bg="#121212",fg="white",font=("Garamond",40,'bold'))
    label.pack(pady=40)

    text=Text(broot,width=60,height=20,font=("Garamond",20,'bold'))
    text.pack(pady=60)

    try:
        with open("transaction.txt","r") as file:
            data=file.read()

            if data:
                text.insert(END,data)
            else:
                text.insert(END, "No Transactions Yet")

    except FileNotFoundError:
        text.insert(END,"No Transactions Yet")

    text.config(state='disabled')




