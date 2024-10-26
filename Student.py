from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face_Recognition_System")

        #*********VARIABLES***********
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        #bg image
        img3 = Image.open(r"Images\backgimage.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=0, width = 1530, height = 710)

        title_lbl = Label(bg_img,text="Student Record System",font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=15,  pady=10  )
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10, y=50, width=1225, height=550)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10 ,width=600, height= 520)

        # img = Image.open(r"D:\projects\Attendance Management System\Images\StPortal.jpg")
        # img = img.resize((450,130), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root , image = self.photoimg)
        # f_lbl.place(x=0, y=0, width = 450, height = 130)

        #Current Course
        Current_course = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        Current_course.place(x=5, y=10,width=510, height= 130)

        #Department
        dep_label = Label(Current_course, text="Department", font=("times new roman",12,"bold"))
        dep_label.grid(row=0, column=0 )
        dep_combo = ttk.Combobox(Current_course, textvariable=self.var_dep, font=("times new roman",12,"bold"), width=17,state="readonly")

        dep_combo["values"]= ("Select Department", "Computer","IT","Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        #Course
        Course_label = Label(Current_course, text="Course", font=("times new roman",12,"bold"))
        Course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_course,textvariable=self.var_course, font=("times new roman",12,"bold"), width=17,state="readonly")
        course_combo["values"]= ("Select Course", "FE","SE","TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(Current_course, text="Year", font=("times new roman",12,"bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(Current_course, textvariable=self.var_year, font=("times new roman",12,"bold"), width=17,state="readonly")
        year_combo["values"]= ("Select year", "2020-21","2021-22","2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)  

        #Semester
        sem_label = Label(Current_course, text="Semester", font=("times new roman",12,"bold"))
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(Current_course,textvariable=self.var_semester, font=("times new roman",12,"bold"), width=17,state="readonly")
        sem_combo["values"]= ("Select Sem", "1","2","3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)  
        
        #Class Student Information
        class_student = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Student Information", font=("times new roman",12,"bold"))
        class_student.place(x=5, y=155, width=510, height= 300)

        #Student ID label
        studentId_label = Label(class_student, text="Student ID:",font=("times new roman",12,"bold")) 
        studentId_label.grid(row=0, column=0, padx=10, sticky = W)

        #student id
        studentID_entry = Entry(class_student,textvariable=self.var_id, width=12, font=("times new roman",12,"bold") )
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        #student name 
        studentName_label = Label(class_student,text="Student Name:", font=("times new roman",12,"bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        studentName_entry = ttk.Entry(class_student, textvariable=self.var_name, width=12,font=("times new roman",12,"bold") )
        studentName_entry.grid(row=0, column=3, padx=10, pady=5,sticky=W)

        #class_division 
        class_division_label = Label(class_student,text="class division:", font=("times new roman",12,"bold"))
        class_division_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)
        # class_division_entry = ttk.Entry(class_student, textvariable=self.var_div,width=12,font=("times new roman",12,"bold") )
        # class_division_entry.grid(row=1, column=1, padx=10, pady=5,sticky=W)

        div_combo = ttk.Combobox(class_student, textvariable=self.var_div, font=("times new roman",12,"bold"), width=10,state="readonly")
        div_combo["values"]= ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)  

        #roll no
        roll_label = Label(class_student,text="Roll No: ", font=("times new roman",12,"bold"))
        roll_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)
        roll_label_entry = ttk.Entry(class_student,textvariable=self.var_roll, width=12,font=("times new roman",12,"bold") )
        roll_label_entry.grid(row=1, column=3, padx=10, pady=5,sticky=W)

        #Gender
        Gender_label = Label(class_student,text="Gender: ", font=("times new roman",12,"bold"))
        Gender_label.grid(row=2, column=0, padx=10, pady=5,sticky=W) 
        # Gender_label_entry = ttk.Entry(class_student, textvariable=self.var_gender, width=12,font=("times new roman",12,"bold") )
        # Gender_label_entry.grid(row=2, column=1, padx=10, pady=5,sticky=W) 
        gender_combo = ttk.Combobox(class_student, textvariable=self.var_gender, font=("times new roman",12,"bold"), width=10,state="readonly")
        gender_combo["values"]= ("female", "male", "other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)  

        #DOB
        dob_label =  Label(class_student,text="DOB: ", font=("times new roman",12,"bold"))
        dob_label .grid(row=2, column=2, padx=10, pady=5,sticky=W)
        dob_label_entry = ttk.Entry(class_student, textvariable=self.var_dob,width=12,font=("times new roman",12,"bold") )
        dob_label_entry.grid(row=2, column=3, padx=10, pady=5,sticky=W)

        
        
        #Email
        email_label = Label(class_student,text="E-mail: ", font=("times new roman",12,"bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5,sticky=W) 
        email_label_entry = ttk.Entry(class_student, textvariable=self.var_email,width=12,font=("times new roman",12,"bold") )
        email_label_entry.grid(row=3, column=1, padx=10, pady=5,sticky=W) 

        #phone no
        phone_label =  Label(class_student,text="Phn Number: ", font=("times new roman",12,"bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5,sticky=W)
        phone_label_entry = ttk.Entry(class_student, textvariable=self.var_phone,width=12,font=("times new roman",12,"bold") )
        phone_label_entry.grid(row=3, column=3, padx=10, pady=5,sticky=W)

        #Address
        Address_label =  Label(class_student,text="Adress: ", font=("times new roman",12,"bold"))
        Address_label.grid(row=4, column=0, padx=10, pady=5,sticky=W)
        Address_label_entry = ttk.Entry(class_student, textvariable=self.var_address,width=12,font=("times new roman",12,"bold") )
        Address_label_entry.grid(row=4, column=1, padx=10, pady=5,sticky=W)

         #Teacher Name
        Teacher_label =  Label(class_student,text="Faculty: ", font=("times new roman",12,"bold"))
        Teacher_label.grid(row=4, column=2, padx=10, pady=5,sticky=W)
        Teacher_label_entry = ttk.Entry(class_student,textvariable=self.var_teacher, width=12,font=("times new roman",12,"bold") )
        Teacher_label_entry.grid(row=4, column=3, padx=10, pady=5,sticky=W)

        #radio buttons
        self.var_radio1 = StringVar()
        Radiobtn1 = ttk.Radiobutton(class_student,variable= self.var_radio1, text="Take Photo Sample", value="Yes")
        Radiobtn1.grid(row=5,column=0)

        Radiobtn2 = ttk.Radiobutton(class_student, variable= self.var_radio1,text="No Photo Sample", value="No")
        Radiobtn2.grid(row=5,column=1)
        
        #button Frame
        btn_frame = Frame(class_student, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=210, width=715,height=50)

#Save button
        save_btn = Button(btn_frame, text="save",
         command=self.add_data,
        width=12, font=("Helvetica", 13, "bold"),bg="#1e3a8a",  fg="#ffffff")
        save_btn.grid(row=0, column=0)
#update button
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=12, font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff")
        update_btn.grid(row=0, column=1)
#delete button
        delete_btn= Button(btn_frame, text="Delete", command=self.delete_data, width=12,font=("Helvetica", 13, "bold"),bg="#1e3a8a",  fg="#ffffff" )
        delete_btn.grid(row=0, column=2)
#reset button
        reset_btn= Button(btn_frame, text="Reset",command=self.reset_data , width=12,font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student, bd=2, bg="white")
        btn_frame1.place(x=0, y=240, width=715, height=35)

        #Take photo button
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=24, command=self.generate_dataset ,   font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff" )
        take_photo_btn.grid(row = 0,column=0)
#update photo button
        update_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=24, font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff" )
        update_photo_btn.grid(row =0,column=1)

         #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=620, y=10 ,width=600, height= 520)

        #=======Search System=======

        #Search_Frame
        Search_Frame= LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        Search_Frame.place(x=5, y=10, width=510, height= 70)
  #Search_lABEL
        search_label = Label(Search_Frame, text="Search By:", font=("times new romFan",12,"bold"))
        search_label.grid(row=0, column=0, padx=10,  pady=5 ,sticky=W)
  #Search_COMBO
        search_combo = ttk.Combobox(Search_Frame, font=("times new roman",12,"bold"), width=10,state="readonly")
        search_combo["values"]= ("Select", "Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10 , sticky=W)
         
         #Search entry
        search_entry = Entry(Search_Frame, width=12, font=("times new roman",12,"bold") )
        search_entry.grid(row=0, column=2, padx=10, sticky=W)

#search button
#indentation
        serach_btn = Button(Search_Frame, text="Search", width=7, font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff" )
        serach_btn.grid(row = 0,column=3, padx=4) #socail distancing
#showLL BUTTON
        ShowAll_btn = Button(Search_Frame, text="Show All", width=7, font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff" )
        ShowAll_btn.grid(row =0,column=4)

        #table frame
        Table_Frame= Frame(Right_frame, bd=2, relief=RIDGE)
        Table_Frame.place(x=5, y=110, width=510, height= 250)

        #scoll bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient = VERTICAL)

        self.student_table = ttk.Treeview(Table_Frame, column=('Dept', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll', 'gender', 'dob', 'email','phone', 'address', 'teacher', 'photo' ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        #pack
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #heading
        self.student_table.heading("Dept", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Sem")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Faculty")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
         #set column widthh
        self.student_table.column('Dept', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('year', width=100)
        self.student_table.column('sem', width=100)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('roll', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('div', width=100)
        self.student_table.column('dob', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('phone', width=100)
        self.student_table.column('address', width=100) 
        self.student_table.column('teacher', width=100)
        self.student_table.column('photo', width=100)

        self.student_table.pack(fill = BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

#===============FUNCTION DECLARATION=========
    def add_data(self):
        if (self.var_dep.get() == "Select Department" or  self.var_name.get() == "" or self.var_id.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else: 
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_id.get(),
                                                                                                              self.var_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                            
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Welcome", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent = self.root)

         #===============FETCH DATA ========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=i)
            conn.commit()
        conn.close()

#========get cursor============
    def get_cursor(self,  event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)    
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #update data funcion
    def update_data(self):
        if self.var_dep.get() ==  "Select Department" or  self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else: 
            try:
                Update = messagebox.askyesno("update","Do you want to update this student details", parent = self.root)
                if Update  > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s, course=%s, year=%s, semester=%s, Name=%s, `div`=%s, rolll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, Photosample=%s Where Student_id=%s",(
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_name.get(),
                                                                                                             self.var_div.get(),
                                                                                                             self.var_roll.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_teacher.get(),
                                                                                                             self.var_radio1.get(),
                                                                                                             self.var_id.get(),
                                                                                                            ))
                else:
                    if  not  Update:
                        return
                messagebox.showinfo("success", "succcessfully data updated", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"DUe To:{str(es)}",parent = self.root)

     #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "student id must be required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this sutdent", parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select Course")
        self.var_year.set("select Year")
        self.var_semester.set("select Semester")
        self.var_id.set("")
        self.var_div.set("select Division")
        self.var_roll.set("")
        self.var_gender.set("Female")
        self.var_dob.set("")
        self.var_email.set("example@gmail.com")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# ================GENERATE DATA SET=================
    def generate_dataset(self):
        if self.var_dep.get() ==  "Select Department" or  self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else: 
            try:
                 conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult = my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("Update student set Dep=%s, course=%s, year=%s, semester=%s, Name=%s, `div`=%s, rolll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, Photosample=%s Where Student_id=%s",(
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_id.get()==id+1,
                                ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()
            

                #LOAD PRDEFIENED DATA OF FACE
                 face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces = face_classifier.detectMultiScale(gray,1.3,5)

                     #scalinng factor =1.3
                     #minimum  neighbour=5

                   for(x,y,w,h) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped
                 cap =  cv2.VideoCapture(0)
                 img_id=0
                 while True:
                   ret,my_frame = cap.read()
                   if face_cropped(my_frame) is not None:
                       img_id +=1
                   face = cv2.resize(face_cropped(my_frame),(450,450))
                   face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                   file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                   cv2.imwrite(file_name_path,face)

                   cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

                # cv2.putText(face,str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0),2)
                   cv2.imshow("Cropped Face",face)

                   if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("Result", "Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)














     



       


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()