from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from datetime import datetime, timedelta
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="green", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #=======FIRST IMAGE==============
        img_top = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        #========SECOND IMAGE============
        img_bottom = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\FACE RECOGNITION ATTENDANCE BASED SYSTEM\college_images\sample (2).jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        #=========BUTTON==============
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="lightgreen", fg="green")
        b1_1.place(x=380, y=620, width=200, height=40)

    #============ATTENDANCE===========================
    def mark_attendance(self, i, r, n, d):    
        with open("priya.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #============FACE RECOGNITION==============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, buffer):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 70:
                    conn = mysql.connector.connect(host="localhost", username="root", password="02cheeku__pari07", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                    result = my_cursor.fetchone()
                    if result:
                        i, n, r, d = result
                        buffer.append((i, r, n, d))
                        if len(buffer) > 10:
                            buffer.pop(0)
                        if len(buffer) == 10 and all(x == buffer[0] for x in buffer):
                            cv2.putText(img, f"Student Id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade, buffer):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, buffer)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        buffer = []

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade, buffer)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()