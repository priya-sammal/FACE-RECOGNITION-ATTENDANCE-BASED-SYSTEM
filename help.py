from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="purple",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\developer2.jpeg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        dev_label=Label( f_lbl,text="EMAIL:priyasammal3@gmail.com",font=("times new roman",13,"bold"),bg="white",fg="purple")
        dev_label.grid(row=0,column=0,padx=625,pady=220,sticky=W)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()