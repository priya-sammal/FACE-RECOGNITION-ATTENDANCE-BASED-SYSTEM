from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help
from tkinter import messagebox
import mysql.connector

def main():
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        img_top = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\clg3.jpg")
        img_top = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDACE BASED SYSTEM", font=("times new roman", 35, "bold"), bg="purple", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ===========FRAME===============
        main_frame = Frame(f_lbl, bd=2, bg="black")
        main_frame.place(x=610, y=170, width=340, height=450)

        # FIRST IMAGE
        img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\LoginIconAppl.png")
        img = img.resize((100, 100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg, bg="black")
        f_lbl.place(x=730, y=175, width=100, height=100)

        get_str = Label(main_frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # ========LABEL================
        username = Label(main_frame, text="Std Id or Clg Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(main_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # =========ICON IMAGES====================
        img2 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2, bg="black")
        f_lbl.place(x=660, y=328, width=25, height=25)

        img3 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\lock-512.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3, bg="black")
        f_lbl.place(x=660, y=398, width=25, height=25)

        # ==========LOGIN BUTTON==============
        loginbtn = Button(main_frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ==============REGISTER BUTTON=====================
        registerbtn = Button(main_frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # ==============FORGET BUTTON=====================
        forgetbtn = Button(main_frame, text="Forget Password",command=self.forget_password_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.obj=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        #elif self.txtuser.get() == "220122300" and self.txtpass.get() == "priya007":
            messagebox.showinfo("Success", "Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="02cheeku__pari07",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE securityA=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Std_Id or Clg_Email & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Attendance_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #===================RESET PASSWORD======================
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select Security Questions",parent=self.root2)
        elif self.security_a_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="02cheeku__pari07",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("SELECT * FROM register WHERE securityA=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txtuser.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where securityA=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Yor password has been reset,Please login with new password",parent=self.root2)
                self.root2.destroy()

    #===============FORGET PASSWORD====================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Student id or Clg email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="02cheeku__pari07",database="face_recognizer")
            my_cursor=conn.cursor()
            quwery=("SELECT * FROM register WHERE securityA=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(quwery,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the valid std id and clg email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                #===========ROW=============================
                security=Label(self.root2,text="Security Questions",font=("times new roman", 15, "bold"),bg="white")
                security.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Student_Id","College Email ID")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)

                security_a=Label(self.root2,text="Security Answer",font=("times new roman", 15, "bold"),bg="white")
                security_a.place(x=50,y=150)

                self.security_a_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_a_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman", 15, "bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=150,y=290)


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

        b1=Button(frame,image=self.photoimg_l,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),bg="white")
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
            messagebox.showinfo("Success","Register Successfully!!",parent=self.root)
    
    #==============LOGIN============================
    def return_login(self):
        self.root.destroy()

class Face_Recognition_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")


        #FIRST IMAGE
        img=Image.open(r"C:/Users/ASUS/OneDrive/Desktop/FACE RECOGNITION ATTENDANCE BASED SYSTEM/college_images/gehu.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #SECOND IMAGE
        img1=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #THIRD IMAGE
        img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\gehu.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #BACKGROUND IMAGE
        img3=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\white.png")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDACE BASED SYSTEM",font=("times new roman",35,"bold"),bg="violet",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #===========TIME=========================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='purple',foreground='white')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #STUDENT BUTTON 
        img4=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\std1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1_1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1_1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #DETECT FACE BUTTON 
        img5=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\det1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1_1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1_1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #ATTENDANCE BUTTON 
        img6=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\att.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1_1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1_1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #HELP DESK BUTTON 
        img7=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\hlp.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1_1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1_1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #TRAIN DATA BUTTON
        img8=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\tra1.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1_1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1_1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Sign Up Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #PHOTO BUTTON
        img9=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\cam.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1_1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1_1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #DEVELOPER BUTTON
        img10=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\dev.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1_1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1_1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #EXIT BUTTON
        img11=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\exi.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1_1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1_1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="violet",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
    
    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("FACE RECOGNITION","Are you sure to exit this project",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return
        
    #===========================FUNCTIONS BUTTONS================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
   main()
