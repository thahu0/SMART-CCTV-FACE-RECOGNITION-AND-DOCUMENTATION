import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import subprocess
import sys

def run_yolo():
    # Call the YOLO object detection program using subprocess
    subprocess.run(["python", "C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/peoplecounteryolov8-main/main.py"])

def run_opencv():
    # Call the OpenCV face recognition program using subprocess
    subprocess.run(["python", "C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/face1/attendence"])


def run_opencv1():
    # Call the OpenCV face recognition program using subprocess
    subprocess.run(["python", "C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/face1/attendance1"])
def exit_program():
    sys.exit()

# Create main window
window = tk.Tk()
window.title("CCTV Documentation with Face Recognition")
window.geometry('600x400')
window.configure(bg="#333333")  # Set background color

# Load background image
bg_image_path = "C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/ICONS/background.png"

bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((2000, 1000))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = tk.Label(window, image=bg_photo)
background_label.place(x=10, y=0, relwidth=1, relheight=1)

# Define custom fonts
title_font = font.Font(family='Helvetica', size=30, weight='bold')
button_font = font.Font(family='Helvetica', size=20, weight='bold')

# Title label
label_title = tk.Label(window, text="CCTV Documentation with Face Recognition", fg="#ffffff", bg="#333333")
label_title['font'] = title_font
label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Load and resize icons
cctv_image = Image.open("C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/ICONS/OIP.jpeg")
cctv_image = cctv_image.resize((100, 100))
cctv_icon = ImageTk.PhotoImage(cctv_image)

face_recognition_image = Image.open("C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/ICONS/FACER.jpg")
face_recognition_image = face_recognition_image.resize((100, 100))
face_recognition_icon = ImageTk.PhotoImage(face_recognition_image)

face_recognition_image1 = Image.open("C:/Users/nuhaj/OneDrive/Desktop/miniprojectfinal/ICONS/recording-icon-png-25.jpg")
face_recognition_image1 = face_recognition_image1.resize((100, 100))
face_recognition_icon1 = ImageTk.PhotoImage(face_recognition_image1)

# Define light blue color with some transparency
light_blue_color = "#e9f1f8"  # Adjust the transparency as needed (80 is the alpha value in hexadecimal)

# Buttons with icons
btn_yolo = tk.Button(window, text='IN AND OUT', command=run_yolo, fg='#333333', bg=light_blue_color, padx=20, pady=10, compound=tk.TOP, image=cctv_icon)
btn_yolo['font'] = button_font
btn_yolo.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

btn_opencv = tk.Button(window, text='Face Recognition live', command=run_opencv, fg='#333333', bg=light_blue_color, padx=20, pady=10, compound=tk.TOP, image=face_recognition_icon)
btn_opencv['font'] = button_font
btn_opencv.place(relx=0.75, rely=0.7, anchor=tk.CENTER)

btn_opencv = tk.Button(window, text='Face Recognition video', command=run_opencv1, fg='#333333', bg=light_blue_color, padx=20, pady=10, compound=tk.TOP, image=face_recognition_icon1)
btn_opencv['font'] = button_font
btn_opencv.place(relx=0.25, rely=0.7, anchor=tk.CENTER)

btn_exit = tk.Button(window, text='Exit', command=exit_program, fg='#333333', bg=light_blue_color, padx=20, pady=10)
btn_exit['font'] = button_font
btn_exit.place(relx=.5, rely=0.9, anchor=tk.CENTER)

window.mainloop()
