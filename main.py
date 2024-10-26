from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
from face_recognition import face_recognition
import os
from Attendance import Attendance
from Train import Train
from developer import Developer
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face_Recognition_System")


        #image 1       
        # img = Image.open(r"D:\projects\Attendance Management System\Images\image1.jpg")
        # img = img.resize((450,130), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root , image = self.photoimg)
        # f_lbl.place(x=0, y=0, width = 450, height = 130)
        
        # #image 2
        # img1 = Image.open(r"D:\projects\Attendance Management System\Images\faceRecognition.jpg")
        # img1 = img1.resize((500,130), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl = Label(self.root , image = self.photoimg1)
        # f_lbl.place(x=450, y=0, width = 500, height = 130)

        # #image 3
        # img2 = Image.open(r"D:\projects\Attendance Management System\Images\image1.jpg")
        # img2 = img2.resize((500,130), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl = Label(self.root , image = self.photoimg2)
        # f_lbl.place(x=900, y=0, width = 450, height = 130)

        #bg image
        img3 = Image.open(r"Images\backgimage.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=0, width = 1530, height = 710)

        title_lbl = Label(bg_img,text = "FACE-TIME ATTENDANCE MANAGER" ,  font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=0,  pady=10)
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student button
        img4 = Image.open(r"Images\student.jpg")
        img4 = img4.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image 
        self.photoimg4 = ImageTk.PhotoImage(img4)


        b1 = Button(bg_img, image = self.photoimg4, command = self.student_details  ,cursor="hand2")
        b1.place(x=200, y=80, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", command = self.student_details  ,cursor="hand2", font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
        b1_1.place(x=200, y=280, width=200, height=40)

        #Detect Face
        img5 = Image.open(r"Images\faceDetect.jpg")
        img5 = img5.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5, cursor="hand2")
        b1.place(x=500, y=80, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Sense", cursor="hand2", command=self.face_sense, font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
        b1_1.place(x=500, y=280, width=200, height=40)

        #Attendance Management
        img6 = Image.open(r"Images\attendance.jpg")
        img6 = img6.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, command=self.attendance_data,cursor="hand2")
        b1.place(x=800, y=80, width=200, height=200)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 16, "bold"), command=self.attendance_data,bg="dark blue", fg="white")  
        b1_1.place(x=800, y=280, width=200, height=40)

      #    #Help desk
      #   img7 = Image.open(r"Images\HDesk.jpg")
      #   img7 = img7.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
      #   self.photoimg7 = ImageTk.PhotoImage(img7)

      #   b1 = Button(bg_img, image = self.photoimg7, cursor="hand2")
      #   b1.place(x=1000, y=80, width=200, height=200)

      #   b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
      #   b1_1.place(x=1000, y=280, width=200, height=40)

        # Train data
        img8 = Image.open(r"Images\TrainAi.jpg")
        img8 = img8.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, cursor="hand2",command=self.Train_data)
        b1.place(x=200, y=350, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 16, "bold"), bg="dark blue", fg="white",command=self.Train_data)  
        b1_1.place(x=200, y=550, width=200, height=40)
        
        #Photos Face button
        img9 = Image.open(r"Images\photos.jpg")
        img9 = img9.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, command= self.open_img, cursor="hand2")
        b1.place(x=500, y=350, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command= self.open_img,font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
        b1_1.place(x=500, y=550, width=200, height=40)
        
        #Developer Face Button
        img10 = Image.open(r"Images\developerFace.jpg")
        img10 = img10.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image = self.photoimg10, cursor="hand2",command= self.Developer_data)
        b1.place(x=800, y=350, width=200, height=200)

        b1_1 = Button(bg_img, text="Developer Face", cursor="hand2", font=("times new roman", 16, "bold"), bg="dark blue", fg="white",command= self.Developer_data)  
        b1_1.place(x=800, y=550, width=200, height=40)

      #   #Exit Button
      #   img11 = Image.open(r"Images\exir.jpg")
      #   img11 = img11.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
      #   self.photoimg11 = ImageTk.PhotoImage(img11)

      #   b1 = Button(bg_img, image = self.photoimg11, cursor="hand2")
      #   b1.place(x=1000, y=350, width=200, height=200)

      #   b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
      #   b1_1.place(x=1000, y=550, width=200, height=40)

      #exit button
      #   exit_button = ttk.Button(root, text="Exit",    command=self.iExit, bg="red", fg="white")
      #   exit_button.place(relx=1.0, rely=0.0, anchor='ne') 


    def open_img(self):
       os.startfile("data")
       


        #=================function btn =================
    def student_details(self):
     self.new_window = Toplevel(self.root)
    #variable to declare classs
     self.app = Student(self.new_window)


    def face_sense(self):
       self.new_window = Toplevel(self.root)
       self.app = face_recognition(self.new_window)

    def attendance_data(self):
       self.new_window = Toplevel(self.root)
       self.app = Attendance(self.new_window)
    
    def Train_data(self):
       self.new_window = Toplevel(self.root)
       self.app = Train(self.new_window)

    def Developer_data(self):
       self.new_window = Toplevel(self.root)
       self.app = Developer(self.new_window)

   #  def iExit(self):
   #     self.iExit = messagebox.askyesno("update","Do you want to update this student details", parent = self.root)
       

     






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    
    root.mainloop()


