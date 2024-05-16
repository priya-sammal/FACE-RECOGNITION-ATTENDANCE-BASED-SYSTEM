from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="violet",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\bg3.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #===========FRAME===============
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\priya.jpg")
        img_top1=img_top1.resize((200,300),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=300)

        #DEVELOPER INFO
        dev_label=Label(main_frame,text="HEY!! MY NAME IS PRIYA SAMMAL",font=("times new roman",13,"bold"),bg="white")
        dev_label.grid(row=0,column=0,padx=0,sticky=W)

        img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\developer1.jpg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=310,width=500,height=390)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()