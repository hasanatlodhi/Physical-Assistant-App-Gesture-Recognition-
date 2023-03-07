import tkinter as tk


class CustomDialog:
    def __init__(self, master, message):
        self.master = master
        self.message = message
        
        # Create a new Toplevel window for the dialog box
        self.top = tk.Toplevel(master)
        self.top.geometry("300x100")
        
        # Add a label to display the message
        self.label = tk.Label(self.top, text=message)
        self.label.pack(padx=10, pady=10)
        
        # Add a button to dismiss the dialog box
        self.button = tk.Button(self.top, text="OK", command=self.ok)
        self.button.pack(padx=10, pady=10)
        
        # Grab the keyboard and mouse focus for the dialog box
        self.top.grab_set()
        
        # Wait for the dialog box to be dismissed
        self.top.wait_window()
    
    def ok(self):
        
        # Dismiss the dialog box
        self.top.destroy()