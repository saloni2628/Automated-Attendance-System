from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_course = StringVar()
        self.var_year=StringVar()
        self.var_std_id = IntVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        # background image
        img1 = Image.open(r"images\pic2.jpeg")
        img1 = img1.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=50, width=1530, height=80)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=140,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Left_frame.place(x=10,y=50,width=750,height=600)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=5,y=5,width=725,height=200)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 14, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=50, pady=55,sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 14, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "MCA", "MCA(AI/DS)", "BCA", "B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 14, "bold"), bg="white")
        year_label.grid(row=0, column=2, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 14, "bold"), state="readonly")
        year_combo["values"] = ("Select year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        #  Class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",font=("times new roman", 14, "bold"))
        class_student_frame.place(x=5, y=210, width=725, height=350)

        #student ID
        id_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 14, "bold"), bg="white")
        id_label.grid(row=0, column=0, padx=8,pady=15, sticky=W)

        id_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman", 14, "bold"))
        id_entry.grid(row=0,column=1,padx=8,pady=5,sticky=W)

        # student name
        name_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 14, "bold"),bg="white")
        name_label.grid(row=0, column=2, padx=8, pady=5, sticky=W)

        name_entry = ttk.Entry(class_student_frame, width=19,textvariable=self.var_std_name, font=("times new roman", 14, "bold"))
        name_entry.grid(row=0, column=3, padx=8, pady=5, sticky=W)

        # roll no.
        roll_no_label = Label(class_student_frame, text="Roll No.:", font=("times new roman", 14, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=8, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_roll,font=("times new roman", 14, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=8, pady=5, sticky=W)

        # Phone no.
        phone_label = Label(class_student_frame, text="Phone No.:", font=("times new roman", 14, "bold"),bg="white")
        phone_label.grid(row=1, column=2, padx=8, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, width=19,textvariable=self.var_phone,font=("times new roman", 14, "bold"))
        phone_entry.grid(row=1, column=3, padx=8, pady=5, sticky=W)

        # gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 14, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=8, pady=5, sticky=W)

        self.var_gender = StringVar()
        radionbtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_gender, text="Male",value="male")
        radionbtn1.grid(row=2, column=1)

        radionbtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_gender, text="Female", value="female")
        radionbtn2.grid(row=2, column=2)


        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 14, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=8, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 14, "bold"))
        email_entry.grid(row=3, column=1, padx=8, pady=5, sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0,padx=8, pady=10)

        radionbtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6, column=1,padx=8, pady=10)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=715,height=56)

        save_btn=Button(btn_frame,text="save",width=16,command=self.add_data,font=("times new roman", 14, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=15, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=15,font=("times new roman", 14, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=16, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=270, width=715, height=50)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=32, font=("times new roman", 14, "bold"), bg="blue",fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample",width=32, font=("times new roman", 14, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0, column=1)

        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 14, "bold"))
        Right_frame.place(x=780, y=50, width=710, height=600)

        #===============================Search System==========================
        search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, bg="white",text="Search system",font=("times new roman", 14, "bold"))
        search_frame.place(x=5, y=10, width=700, height=100)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 14, "bold"),bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 14, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=12, font=("times new roman", 14, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=8, font=("times new roman", 14, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=4)

        showall_btn = Button(search_frame, text="Show All", width=8, font=("times new roman", 14, "bold"), bg="blue",fg="white")
        showall_btn.grid(row=0, column=4, padx=4)

        #===========table frame========================================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=110,width=700,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("course","year","id","name","roll","gender","email","phone","radio1"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("phone", text="Phone no")
        self.student_table.heading("radio1", text="Photo Sample")
        self.student_table["show"]="headings"

        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("radio1", width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #functiom declaration
    def add_data(self):
            if self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("ERROR","All fields are required",parent=self.root)
            else:
                try:
                   conn=mysql.connector.connect(host="localhost",username="root",password="Admin@22",database="attendance")
                   my_cursor=conn.cursor()
                   my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_course.get(),self.var_year.get(),self.var_std_id.get(),self.var_std_name.get(),
                                     self.var_roll.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get()))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success","Student details has been addes succesfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
           conn = mysql.connector.connect(host="localhost", username="root", password="Admin@22", database="attendance")
           my_cursor = conn.cursor()
           my_cursor.execute("select * from student")
           data=my_cursor.fetchall()
           if len(data)!=0:
               self.student_table.delete(*self.student_table.get_children())
               for i in data:
                   self.student_table.insert("",END,values=i)
               conn.commit()
           conn.close()

    #get_cursor funtion
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_course.set(data[0])
        self.var_year.set(data[1])
        self.var_std_id.set(data[2])
        self.var_std_name.set(data[3])
        self.var_roll.set(data[4])
        self.var_gender.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])
        self.var_radio1.set(data[8])

    #update data
    def update_data(self):
        if self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("ERROR", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if(update>0):
                    conn = mysql.connector.connect(host="localhost", username="root", password="Admin@22",database="attendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set course=%s,Year=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",
                                      (self.var_course.get(), self.var_year.get(),self.var_std_name.get(),self.var_roll.get(),self.var_gender.get(),self.var_email.get(),
                                      self.var_phone.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #delete funtion
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Admin@22",database="attendance")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_course.set("Select Department")
        self.var_course.set("Select year")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

   #======================Generate data set or Take photo sample
    def generate_dataset(self):
        if self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("ERROR", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Admin@22",database="attendance")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set course=%s,Year=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",(self.var_course.get(), self.var_year.get(),
                                self.var_std_name.get(), self.var_roll.get(),self.var_gender.get(), self.var_email.get(),self.var_phone.get(), self.var_radio1.get(), self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load  predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3, minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()