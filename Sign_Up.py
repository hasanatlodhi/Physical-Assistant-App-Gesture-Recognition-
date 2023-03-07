import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from custom_dialog import CustomDialog
class SignupApp:
    def __init__(self):
        self.data=pd.read_csv('users.csv')
        self.master =  tk.Tk()
        self.master.title("Doctor Signup")
        self.master.geometry("500x500")
        self.master.config(bg="#ffffff")
        self.master.resizable(False,False)

        # Add background image
        self.bg_img = Image.open("background.jpg")
        self.bg_img = self.bg_img.resize((500, 500), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.master, image=self.bg_img)
        self.bg_label.place(x=0, y=0)

        # Add doctor signup form
        self.label = tk.Label(self.master, text="Doctor Signup", font=("Arial", 20), bg="#ffffff")
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.master, text="Doctor Id", font=("Arial", 14), bg="#ffffff")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.master, font=("Arial", 14))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.master, text="Password", font=("Arial", 14), bg="#ffffff")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.master, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=10)

        # self.confirm_password_label = tk.Label(self.master, text="Confirm Password", font=("Arial", 14), bg="#ffffff")
        # self.confirm_password_label.pack(pady=10)

        # self.confirm_password_entry = tk.Entry(self.master, font=("Arial", 14), show="*")
        # self.password_entry.pack(pady=10)

        self.signup_btn = tk.Button(self.master, text="Sign-Up", font=("Arial", 14), bg="#378c35", fg="#ffffff")
        self.signup_btn.pack(pady=10)
        self.login_btn = tk.Button(self.master, text="Login?", font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.login_btn.pack(pady=10)

        # Add login button functionality
        self.login_btn.bind("<Button-1>", self.login)
        self.signup_btn.bind("<Button-1>", self.sign_up)

        self.master.mainloop()

    def sign_up(self,event):
        id= self.username_entry.get()
        passw=self.password_entry.get()
        if id=="" or passw=="":
            CustomDialog(self.master,"Please Fill all the fields")
            return
        if len(passw)<8:
            CustomDialog(self.master,"Password Should be more than 8 characters")
            return

        for i in self.data['doctorsid'].values:
            if int(id)==int(i):
                CustomDialog(self.master,"ID already exists please choose a different one")
                return 
            new_row = pd.Series({'doctorsid': id, 'password': passw})
            self.data=self.data.append(new_row, ignore_index=True)
            self.data.to_csv('users.csv', index=False, header=['doctorsid', 'password'])
            CustomDialog(self.master,"Recorded Added Successfully")
            self.master.destroy()
            from Main_App import LoginApp
            LoginApp()
    def login(self,event):
        self.master.destroy()
        from Main_App import LoginApp
        LoginApp()