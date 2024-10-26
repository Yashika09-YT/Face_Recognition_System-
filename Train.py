from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
from cv2 import face
import os
import numpy as np
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face Recognition System")
        #bg image
        img3 = Image.open(r"Images\backgimage.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=0, width = 1530, height = 710)

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=15,  pady=10 )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #image
        img_top= Image.open(r"Images\FaceReco.jpg")
        img_top = img_top.resize((300,300), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg = ImageTk.PhotoImage(img_top)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=500, y=100, width=300, height=300)

        #button
        b1_1 = Button(self.root, text="Train Data", cursor="hand2", command= self.train_classifier,font=("times new roman", 16, "bold"), bg="dark blue", fg="white")  
        b1_1.place(x=500, y=400, width=300, height=40)

    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Gray scale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # ====== train the classifier and save ======
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data completed")

# Main block to run the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
