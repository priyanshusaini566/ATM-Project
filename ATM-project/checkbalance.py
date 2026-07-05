from tkinter import *

def balance():
    new_root = Toplevel()
    new_root.title("Check Balance Page")
    new_root.geometry("600x400") # Ek clean size de dete hain
    new_root.config(bg="white")
    
    # File se current balance read karein
    current_balance = 0
    try:
        with open("balance.txt", "r") as file:
            content = file.read().strip()
            if content:
                current_balance = int(content)
    except FileNotFoundError:
        current_balance = 0 # Agar account naya hai toh balance 0 dikhayega

    label1 = Label(new_root, fg="black", bg="white", text="Your Current Balance is:", font=("Garamond", 30, 'bold'))
    label1.pack(pady=40)

    # Balance ko label2 par show karein
    label2 = Label(new_root, text=f"Rs. {current_balance}", bg="white", fg="#00CC66", font=("Segoe UI", 40, 'bold'))
    label2.pack(pady=20)
    
    # Close button
    btn_close = Button(new_root, text="Close", font=("Garamond", 15, 'bold'), bg="#121212", fg="white", command=new_root.destroy)
    btn_close.pack(pady=20)