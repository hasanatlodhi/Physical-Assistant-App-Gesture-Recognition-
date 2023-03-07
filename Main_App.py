import tkinter as tk
from PIL import ImageTk, Image
from custom_dialog import CustomDialog
from Sign_Up import SignupApp
import pandas as pd
from Start_App import StartApp
class LoginApp:
    def __init__(self):
        
        self.data=pd.read_csv('users.csv')
        self.master = tk.Tk()
        self.master.title("Doctor Login")
        self.master.geometry("500x500")
        self.master.config(bg="#ffffff")
        self.master.resizable(False,False)

        # Add background image
        self.bg_img = Image.open("background.jpg")
        self.bg_img = self.bg_img.resize((500, 500), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.master, image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # Add doctor login form
        self.label = tk.Label(self.master, text="Doctor Login", font=("Arial", 20), bg="#ffffff")
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.master, text="Enter Id", font=("Arial", 14), bg="#ffffff")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.master, font=("Arial", 14))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.master, text="Enter Password", font=("Arial", 14), bg="#ffffff")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.master, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self.master, text="Login", font=("Arial", 14), bg="#378c35", fg="#ffffff")
        self.login_button.pack(pady=10)

        self.signup_btn = tk.Button(self.master, text="Sign Up?", font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.signup_btn.pack(pady=10)

        # Add login button functionality
        self.login_button.bind("<Button-1>", self.login)
        self.signup_btn.bind("<Button-1>", self.sign_up)
        
        self.master.mainloop()
    def login(self, event):
        # TODO: Implement login functionality
        userid = self.username_entry.get()
        password = self.password_entry.get()

        if userid == "" or password == "":
            CustomDialog(self.master,"Please Make sure to fill all fields")
            return 
        else:
            found=False
            for index, row in self.data.iterrows():
                id = row['doctorsid']
                passw = row['password']
                if int(id)==int(userid) and password==passw:
                    found=True
                    CustomDialog(self.master,"Login Successfull!")
                    self.master.destroy()
                    StartApp()
            if not found:
                CustomDialog(self.master,"User Doesn't Exist")
    def sign_up(self, event):
        self.master.destroy()
        SignupApp()

LoginApp()