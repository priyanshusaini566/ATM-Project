from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import forgot
import dashboard

root = Tk()
root.geometry("1920x1080")
root.title("Welcome to the ATM")
root.config(bg= "#121212")
lab=Label(root,text="Welcome to the ATM",bg="#121212",fg="white",font=("Segoe UI",40,'bold'))
lab.pack(pady=30)


main_frame=Frame(root,bg="#1E1E1E")
main_frame.pack(pady=10)

img=Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_k2u9ctk2u9ctk2u9.png")
img=img.resize((400,300))
photoimg=ImageTk.PhotoImage(image=img)

main_label=Label(main_frame,image=photoimg)
main_label.pack(pady=10)

pass_frame=Frame(main_frame,bg="#1E1E1E")
pass_frame.pack(pady=10)
pass_label=Label(pass_frame,text="Enter PIN :",bg="#1E1E1E",fg="white",font=("Segoe UI",20,'bold'))
pass_label.pack(side=LEFT)
pass_entry=Entry(pass_frame,bg="#2D2D2D",fg="white",font=("Segoe UI",20,'bold'),show="*")
pass_entry.pack(side=LEFT,padx=10)


def login_verify():
    pin=pass_entry.get().strip()
    if pin=="":
        messagebox.showerror("Error !!","Enter proper details")
        return
    try:
        with open("database.txt","r") as file:
            data=file.readlines()
        found=False

        for line in data:
             pintu=line.strip()

             if pintu==pin:
                 found=True
                 break

        if found:
                messagebox.showinfo("Welcome","Login successful")
                root.withdraw()
                dashboard.options()

        else:
                messagebox.showinfo("Error","PIN is incorrect")

    except FileNotFoundError:
        messagebox.showerror("Error!","No details found")

def forgot_verify():
    forgot.newinterface()


login_btn=Button(main_frame,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),width=10,text="Login",command=login_verify)
login_btn.pack(side=LEFT,padx=42);

forgot_btn=Button(main_frame,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),width=10,text="Forgot PIN",command=forgot_verify)
forgot_btn.pack(side=LEFT,padx=10);


root.mainloop()
