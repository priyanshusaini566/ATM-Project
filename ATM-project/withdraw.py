from tkinter import *
from tkinter import messagebox
from datetime import datetime

def nikalo():

    aroot = Toplevel()
    aroot.geometry("1900x1080")
    aroot.title("withdraw box")
    aroot.config(bg="black")
    lb = Label(aroot, text="Welcome to the withdraw section !!",
               font=("Garamond", 60, "bold"), fg="white",bg="black")
    lb.pack(pady=60)

    m_frame = Frame(aroot, bg="ivory")
    m_frame.pack(pady=20)

    lb2 = Label(m_frame, text="Enter the amount to withdraw",
                fg="black", font=("Garamond", 40, "bold"),bg="ivory")
    lb2.pack(pady=20)

    entry1 = Entry(m_frame, fg="black", bg="white",
                   font=("Garamond", 30, "bold"))
    entry1.pack(pady=10)

    bt_frame=Frame(aroot,bg="black")
    bt_frame.pack(pady=20)


    def bt1_fxn():
        entry1.delete(0,END)
        entry1.insert(0,"500 Rs.")

    def bt2_fxn():
        entry1.delete(0,END)
        entry1.insert(0,"1000 Rs.")

    def bt3_fxn():
        entry1.delete(0,END)
        entry1.insert(0,"2000 Rs.")

    def bt4_fxn():
        entry1.delete(0,END)
        entry1.insert(0,"5000 Rs.")

    def withdraw_btn_fxn():
        w_amount=entry1.get().strip()
        real_amount="".join(filter(str.isdigit,w_amount))

        if int(real_amount)<=0 and not real_amount:
            messagebox.showerror("Error !!","Enter the valid number !!")
            return 
        
        amount=int(real_amount)
        current_amount=0
       
        try:
            with open("balance.txt","r") as file:
                content=file.read().strip()

                if content:
                    current_amount=int(content)

        except FileNotFoundError:
            current_amount=0

        if amount>current_amount:
            messagebox.showerror("Error !!","Insufficient balance")
            return 
        
        new_balance=current_amount-amount
        with open("balance.txt","w") as file:
            file.write(str(new_balance))

        with open("transaction.txt","a") as file:
          file.write(f"{datetime.now():%d-%m-%Y %H:%M:%S} | withdraw | -Rs. {amount}\n")

        messagebox.showinfo("hurray!!",f"{amount} Rs. withdraw successfully")
        aroot.destroy()

    


    bt1=Button(bt_frame,text="500 Rs.",fg="black",width=10,font=("Garamond",30,'bold'),bg="ivory",command=bt1_fxn)
    bt1.pack(side=LEFT)

    bt2=Button(bt_frame,text="1000 Rs.",fg="black",width=10,font=("Garamond",30,'bold'),bg="ivory",command=bt2_fxn)
    bt2.pack(side=LEFT,padx=20)

    bt_frame2=Frame(aroot,bg="black")
    bt_frame2.pack(pady=20)

    bt3=Button(bt_frame2,text="2000 Rs.",fg="black",width=10,font=("Garamond",30,'bold'),bg="ivory",command=bt3_fxn)
    bt3.pack(side=LEFT)

    bt4=Button(bt_frame2,text="5000 Rs.",fg="black",width=10,font=("Garamond",30,'bold'),bg="ivory",command=bt4_fxn)
    bt4.pack(side=LEFT,padx=20)

    bt_frame3=Frame(aroot,bg="black")
    bt_frame3.pack(pady=20)

    withdraw_btn=Button(bt_frame3,text="withdraw",fg="black",width=10,font=("Garamond",30,'bold'),bg="ivory",command=withdraw_btn_fxn)
    withdraw_btn.pack(side=LEFT)
