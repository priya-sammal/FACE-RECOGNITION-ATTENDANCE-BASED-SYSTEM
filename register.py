from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        #===========TEXT VARIABLE==============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        
        #==========BACKGROUND IMAGE=============
        img_top = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\clg.jpg")
        img_top = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        #==========LEFT IMAGE=============
        img_left = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\gehul.jpg")
        img_top_left = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl1 = Label(self.root, image=self.photoimg_left)
        f_lbl1.place(x=50, y=100, width=470, height=550)

        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDACE BASED SYSTEM", font=("times new roman", 35, "bold"), bg="purple", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=======LABEL AND ENTRY=======================
        #==========ROW 1============================
        fname=Label(frame,text="First Name",font=("times new roman", 15, "bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman", 15, "bold"),bg="white")
        l_name.place(x=370,y=100)

        l_name_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        l_name_entry.place(x=370,y=130,width=250)

        #==================ROW 2=================================
        contact=Label(frame,text="Contact No.",font=("times new roman", 15, "bold"),bg="white")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman", 15, "bold"),bg="white")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)

        #===========ROW 3=============================
        security=Label(frame,text="Security Questions",font=("times new roman", 15, "bold"),bg="white")
        security.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Student_Id","College Email ID")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)

        security_a=Label(frame,text="Security Answer",font=("times new roman", 15, "bold"),bg="white")
        security_a.place(x=370,y=240)

        self.security_a_entry=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.security_a_entry.place(x=370,y=270,width=250)

        #==================ROW 4=================================
        pswd=Label(frame,text="Password",font=("times new roman", 15, "bold"),bg="white")
        pswd.place(x=50,y=310)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        pswd_entry.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman", 15, "bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        confirm_pswd_entry.place(x=370,y=340,width=250)

        #===========CHECKBOXES========================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the terms & conditions",font=("times new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #==========BUTTONS=========================
        #======REGISTER===================
        img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\register-now-button1.jpg")
        img = img.resize((200,50), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),bg="white")
        b1.place(x=50,y=420,width=200)

        #=============LOGIN=================
        img_l = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\loginpng.png")
        img_l = img_l.resize((200,40), Image.LANCZOS)
        self.photoimg_l = ImageTk.PhotoImage(img_l)

        b1=Button(frame,image=self.photoimg_l,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),bg="white")
        b1.place(x=330,y=420,width=200)

    #=============FUNCTION DECLARATION================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securitya.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same!!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the our terms and conditions")
        else:
            #messagebox.showinfo("Success","Welcome")
            conn=mysql.connector.connect(host="localhost",username="root",password="02cheeku__pari07",database="face_recognizer")
            my_cursor=conn.cursor()
            qwery=("SELECT * FROM register WHERE email=%s")
            value=(self.var_email.get())
            my_cursor.execute(qwery, (value,))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                  self.var_fname.get(),
                                  self.var_lname.get(),
                                  self.var_contact.get(),
                                  self.var_email.get(),
                                  self.var_securityq.get(),
                                  self.var_securitya.get(),
                                  self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully!!")


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()