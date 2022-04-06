import tkinter.messagebox
from time import strftime
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        #background image
        img1 = Image.open(r"images\pic2.jpeg")
        img1 = img1.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=50,width=1530,height=100)

        def time():
            string = strftime("%H:%M:%S %p")
            lb1.config(text=string)
            lb1.after(100, time)

        lb1 = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='red')
        lb1.place(x=0,y=-20,width=110,height=50)
        time()

        #student photo
        img2 = Image.open(r"images\pic1.png")
        img2 = img2.resize((270, 300), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=250,width=270,height=300)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=550,width=270,height=40)

        # face detection photo
        img3 = Image.open(r"images\pic3.jpg")
        img3 = img3.resize((270, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image=self.photoimg3, cursor="hand2",command=self.face_data)
        b1.place(x=420, y=250, width=270, height=300)

        b1_1 = Button(bg_img, text="Face Detection",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        b1_1.place(x=420, y=550, width=270, height=40)

        # attendance photo
        img4 = Image.open(r"images\pic4.jpg")
        img4 = img4.resize((270, 300), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,command=self.attendance_data, image=self.photoimg4, cursor="hand2")
        b1.place(x=740, y=250, width=270, height=300)

        b1_1 = Button(bg_img, text="Attendance",command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        b1_1.place(x=740, y=550, width=270, height=40)

        # exit photo
        img5 = Image.open(r"images\pic5.jpg")
        img5 = img5.resize((270, 300), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,command=self.iExit,cursor="hand2")
        b1.place(x=1060, y=250, width=270, height=300)

        b1_1 = Button(bg_img, text="Exit",command=self.iExit, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=1060, y=550, width=270, height=40)

        b1_1 = Button(bg_img, text="Train Data",command=self.train_data, cursor="hand2", font=("times new roman", 10, "bold"), bg="lightblue",fg="black")
        b1_1.place(x=1300, y=750, width=100, height=40)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 10, "bold"), bg="lightblue",fg="black")
        b1_1.place(x=1420, y=750, width=100, height=40)

    def open_img(self):
        os.startfile("data")

    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return







if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()