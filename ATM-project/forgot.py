from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def newinterface():
    sub_root=Toplevel()
    sub_root.geometry("1920x1080")
    sub_root.title("Forgot PIN")
    sub_root.config(bg="#121212")

    main_frame=Frame(sub_root,bg="#1E1E1E")
    main_frame.pack(pady=20)
    img=Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_k2u9ctk2u9ctk2u9.png")
    img=img.resize((400,300))
    photoimg=ImageTk.PhotoImage(img)

    main_label=Label(main_frame,image=photoimg)
    main_label.image=photoimg
    main_label.pack(pady=10)

    mno_frame=Frame(main_frame,bg="#1E1E1E")
    mno_frame.pack(pady=10)
    mno_label=Label(mno_frame,text="Mobile Number :  ",bg="#1E1E1E",fg="white",font=("Segoe UI",20,'bold'))
    mno_label.pack(side=LEFT)
    mno_entry=Entry(mno_frame,bg="#2D2D2D",fg="white",font=("Segoe UI",20,'bold'))
    mno_entry.pack(side=LEFT,padx=10)

    pin_frame=Frame(main_frame,bg="#1E1E1E")
    pin_frame.pack(pady=10)
    pin_label=Label(pin_frame,text="Enter new PIN :     ",bg="#1E1E1E",fg="white",font=("Segoe UI",20,'bold'))
    pin_label.pack(side=LEFT)
    pin_entry=Entry(pin_frame,bg="#2D2D2D",fg="white",font=("Segoe UI",20,'bold'))
    pin_entry.pack(side=LEFT,padx=10)

    pin2_frame=Frame(main_frame,bg="#1E1E1E")
    pin2_frame.pack(pady=10)
    pin2_label=Label(pin2_frame,text="Confirm new PIN :",bg="#1E1E1E",fg="white",font=("Segoe UI",20,'bold'))
    pin2_label.pack(side=LEFT)
    pin2_entry=Entry(pin2_frame,bg="#2D2D2D",fg="white",font=("Segoe UI",20,'bold'))
    pin2_entry.pack(side=LEFT,padx=10)

    def pin_verify():
        pin=pin_entry.get().strip()
        pin2=pin2_entry.get().strip()
        if len(pin)!=4:
            messagebox.showerror("Error!!","PIN should have 4 number",parent=sub_root)
            sub_root.lift()
            sub_root.focus_force()


        elif pin!=pin2:
             messagebox.showerror("Error!!","Both PIN number entries should be same",parent=sub_root)
             sub_root.lift()
             sub_root.focus_force()

        else:
            with open("database.txt","a") as file:
                file.write(f"{pin}\n")

            messagebox.showinfo("Hurray!!","PIN reset successfully",parent=sub_root)
            sub_root.destroy()


    reset_btn=Button(main_frame,text="Reset new PIN",width=15,bg="#00CC66",fg="black" ,font=("Garamond",20,'bold'),command=pin_verify)
    reset_btn.pack(pady=10);



