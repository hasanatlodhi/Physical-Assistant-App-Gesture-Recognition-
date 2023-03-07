import tkinter as tk
from MouseMovement import Gesture_System
import threading

class StartApp:
    def __init__(self):
        self.stop_event = threading.Event()
        self.t = threading.Thread(target=Gesture_System,args=(self.stop_event,))
        self.t.start()
        
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.title("Medical Images Options")

        # Set the window size
        self.window.geometry("700x400")

        # Set the background color of the window
        self.window.config(bg="#f5f5f5")

        # Create a label for the options
        options_label = tk.Label(self.window, text="Choose an option:", font=("Arial", 14), bg="#f5f5f5")
        options_label.pack(pady=10)

        # Create a frame to hold the buttons
        options_frame = tk.Frame(self.window, bg="#f5f5f5")
        options_frame.pack()

        # Create the X_ray button
        xray_button = tk.Button(options_frame, text="Small Finger for X_ray", font=("Arial", 12), bg="#ff9933", padx=20, pady=10)
        xray_button.pack(side=tk.TOP, pady=10)

        # Create the Medical_images button
        med_button = tk.Button(options_frame, text="Small and Ring Finger for Medical Images", font=("Arial", 12), bg="#ff3399", padx=20, pady=10)
        med_button.pack(side=tk.TOP, pady=10)

        # Create the Emergency button
        emergency_button = tk.Button(options_frame, text="Last Three Fingers for Emergency", font=("Arial", 12), bg="#3333ff", padx=20, pady=10)
        emergency_button.pack(side=tk.TOP, pady=10)

        patients_btn = tk.Button(options_frame, text="Four Fingers for Patients Records", font=("Arial", 12), bg="#e0a709", padx=20, pady=10)
        patients_btn.pack(side=tk.TOP, pady=10)
        # Start the tkinter event loop
        self.window.mainloop()
        
    def on_close(self):
        self.stop_event.set()
        self.t.join()
        self.window.destroy()

StartApp()
        