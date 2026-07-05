from tkinter import *
from PIL import Image,ImageTk
import checkbalance
import deposit
import withdraw
import transaction

def options():
    sub_root=Toplevel()
    sub_root.geometry("1920x1080")
    sub_root.title("Dashboard")
    sub_root.config(bg="#121212")
    
    lab=Label(sub_root,text="Welcome to the dashboard",font=("Arial",40,'bold'),bg="#121212",fg="white")
    lab.pack(pady=10)

    main_frame=Frame(sub_root,bg="#1E1E1E")
    main_frame.pack(pady=10)

    img=Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_k2u9ctk2u9ctk2u9.png")
    img=img.resize((400,300))
    photoimg=ImageTk.PhotoImage(img)

    main_label=Label(main_frame,image=photoimg)
    main_label.image=photoimg
    main_label.pack(pady=10)

    def btn1_verify():
        checkbalance.balance()

    def activate_deposit():
        deposit.activate()

    def again():
        withdraw.nikalo()

    def hisaab():
        transaction.vasooli()

        



    button1=Button(main_frame,text="Check Balance",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),command=btn1_verify)
    button1.pack(pady=10)

    button2=Button(main_frame,text="Deposit",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),command=activate_deposit)
    button2.pack(pady=10)

    button3=Button(main_frame,text="Withdraw",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),command=again)
    button3.pack(pady=10)

    button4=Button(main_frame,text="Transaction History",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),command=hisaab)
    button4.pack(pady=10)

    button5=Button(main_frame,text="Change PIN",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'))
    button5.pack(pady=10)

    button6=Button(main_frame,text="Logout",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'))
    button6.pack(pady=10)


