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
from login import Login_Window



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

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_Attendance_System(root)
    root.mainloop()
    