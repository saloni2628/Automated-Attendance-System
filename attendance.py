from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import  os
import csv
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = IntVar()
        self.var_atten_course = StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance= StringVar()


        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=80, width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 15, "bold"))
        Left_frame.place(x=10, y=15, width=730, height=580)

        left_inside_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=35, y=135, width=680, height=370)

        # label and entries
        # attendance id

        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 13, "bold"),
                                   bg="white", fg="black")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll
        rollLabel=Label(left_inside_frame, text="Roll:", font="comicsansns 11 bold", bg="white")
        rollLabel.grid(row=0, column=2, padx=4, pady=8, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # name
        nameLabel = Label(left_inside_frame, text="Name:", font="comicsansns 11 bold", bg="white")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # course
        courseLabel = Label(left_inside_frame, text="Course:", font="comicsansns 11 bold", bg="white")
        courseLabel.grid(row=1, column=2)

        atten_course = ttk.Entry(left_inside_frame,textvariable=self.var_atten_course,width=22, font="comicsansns 11 bold")
        atten_course.grid(row=1, column=3, pady=8)

        # time
        timeLabel = Label(left_inside_frame, text="Time:", font="comicsansns 11 bold", bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time, width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # date
        dateLabel = Label(left_inside_frame, text="Date:", font="comicsansns 11 bold", bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", font="comicsansns 11 bold", bg="white")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)



        import_btn = Button(btn_frame, text="Import CSV",width=17,command=self.importCsv,font=("times new roman", 13, "bold"), bg="blue",fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,                                                                                                                                                           width=17, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 15, "bold"))
        Right_frame.place(x=750, y=15, width=730, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        # =============================scroll bar=======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame,column=("id", "roll", "name", "course", "time", "date", "attendance"),
                                                 xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("course", text="Course")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable["show"] = "headings"

        self.AttendaceReportTable.column("id", width=100)
        self.AttendaceReportTable.column("roll", width=100)
        self.AttendaceReportTable.column("name", width=100)
        self.AttendaceReportTable.column("course", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #================face data===================================
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchData(mydata)


     #export
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL Files", "*.*")), parent=root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_course.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_course.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()