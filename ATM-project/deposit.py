from tkinter import *
from tkinter import messagebox
from datetime import datetime

def activate():
    sub_root=Toplevel()
    sub_root.geometry("1920x1080")
    sub_root.title("Deposit section")
    sub_root.config(bg="#121212")
    label=Label(sub_root,text="Welcome to the deposit section !!",font=("Garamond",60,'bold'),bg="#121212",fg="white")
    label.pack(pady=60)

    main_frame=Frame(sub_root,bg="ivory")
    main_frame.pack(pady=20)
    label1=Label(main_frame,text="Enter the amount to deposit :",font=("Garamond",40,'bold'),bg="ivory",fg="black")
    label1.pack(pady=40)

    entry=Entry(main_frame,fg="black",bg="white",font=("Garamond",30,'bold'),width=15)
    entry.pack(pady=20)

    btn_frame=Frame(sub_root,bg="#121212")
    btn_frame.pack(pady=20)

    def btn1_fxn():
        entry.delete(0,END)
        entry.insert(0,"500 RS.")
    def btn2_fxn():
        entry.delete(0,END)
        entry.insert(0,"1000 RS.")
    def btn3_fxn():
        entry.delete(0,END)
        entry.insert(0,"2000 RS.")
    def btn4_fxn():
        entry.delete(0,END)
        entry.insert(0,"5000 RS.")

    btn1=Button(btn_frame,text="500 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn1_fxn)
    btn1.pack(side=LEFT)
    btn2=Button(btn_frame,text="1000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn2_fxn)
    btn2.pack(side=LEFT,padx=20)

    btn2_frame=Frame(sub_root,bg="#121212")
    btn2_frame.pack(pady=10)

    btn3=Button(btn2_frame,text="2000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn3_fxn)
    btn3.pack(side=LEFT)
    btn4=Button(btn2_frame,text="5000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn4_fxn)
    btn4.pack(side=LEFT,padx=20)

    def deposit():
       amount_str = entry.get().strip()
    
    # "500 RS." mein se sirf 500 nikalne ke liye
    # Agar user ne khud type kiya hai toh sirf digits lein
       amount_digits = ''.join(filter(str.isdigit, amount_str))
    
       if not amount_digits or int(amount_digits) <= 0:
           messagebox.showerror("Error!!", "Enter a valid amount!!")
           return
    
       amount = int(amount_digits)

    # Purana balance read karein, agar file nahi hai toh 0 maanein
       current_balance = 0
       try:
           with open("balance.txt", "r") as file:
            content = file.read().strip()
            if content:
                current_balance = int(content)
       except FileNotFoundError:
        current_balance = 0

    # Naya balance calculate karke save karein
       new_balance = current_balance + amount
       with open("balance.txt", "w") as file:  # "w" se purana balance overwrite hoga naye se
          file.write(str(new_balance))

       with open("transaction.txt","a") as file:
          file.write(f"{datetime.now():%d-%m-%Y %H:%M:%S} | Deposit   | +Rs. {amount}\n")

       messagebox.showinfo("Hurray!!", f"{amount} Rs. deposited successfully!")
       sub_root.destroy()


    btn3_frame=Frame(sub_root,bg="#121212")
    btn3_frame.pack(pady=10)

    
        
        

    btn5=Button(btn3_frame,text="Deposit",bg="ivory",fg="black",font=("Garamond",30,'bold'),command=deposit)
    btn5.pack(side=LEFT,padx=20)

    sub_root.deiconify()