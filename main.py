import tkinter as tk
import os

def open_image_steganography():
    os.system("python image.py")

def open_audio_steganography():
    os.system("python audio.py")

# GUI Setup
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("600x400")

label = tk.Label(root, text="Choose Steganography Mode", font=("Arial", 18, "bold"))
label.pack(pady=20)

image_btn = tk.Button(root, text="Image Steganography", command=open_image_steganography, font=("Arial", 14), bg="lightblue", width=30, height=2)
image_btn.pack(pady=20)

audio_btn = tk.Button(root, text="Audio Steganography", command=open_audio_steganography, font=("Arial", 14), bg="lightgreen", width=30, height=2)
audio_btn.pack(pady=20)

exit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="red", width=30, height=2)
exit_btn.pack(pady=20)

root.mainloop()
