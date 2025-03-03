import os
import wave
import numpy as np
from tkinter import filedialog, simpledialog, messagebox, Tk, Label, Button

PASSWORD_FILE = "audio_password.txt"

# Function to save the password
def save_password(password):
    with open(PASSWORD_FILE, "w") as file:
        file.write(password)

# Function to load the saved password
def load_password():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return file.read().strip()
    return ""

def encode_audio():
    audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("WAV files", "*.wav")])
    if not audio_path:
        messagebox.showerror("Error", "No audio file selected!")
        return

    message = simpledialog.askstring("Input", "Enter secret message:", show=None)
    password = simpledialog.askstring("Input", "Enter a passcode:", show="*")
    
    if not message or not password:
        messagebox.showerror("Error", "Message or password cannot be empty!")
        return
    
    save_password(password)
    
    try:
        audio = wave.open(audio_path, mode="rb")
        audio_array = bytearray(list(audio.readframes(audio.getnframes())))
        
        message += int((len(audio_array) - (len(message) * 8 * 8)) / 8) * '#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))
        
        for i, bit in enumerate(bits):
            audio_array[i] = (audio_array[i] & 254) | bit
        
        output_path = os.path.join(os.path.dirname(audio_path), r"C:\Users\Vemul\Downloads\Stenography-main\encryptes_audio.wav")
        new_audio = wave.open(output_path, 'wb')
        new_audio.setparams(audio.getparams())
        new_audio.writeframes(bytes(audio_array))
        new_audio.close()
        audio.close()
        
        messagebox.showinfo("Success", f"Message encoded and saved at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Encoding Failed: {str(e)}")

def decode_audio():
    audio_path = filedialog.askopenfilename(title="Select Encoded Audio File", filetypes=[("WAV files", "*.wav")])
    if not audio_path:
        messagebox.showerror("Error", "No audio file selected!")
        return
    
    saved_password = load_password()
    user_password = simpledialog.askstring("Input", "Enter passcode for decryption:", show="*")
    
    if user_password != saved_password:
        messagebox.showerror("Error", "Incorrect password!")
        return
    
    try:
        audio = wave.open(audio_path, mode="rb")
        audio_array = bytearray(list(audio.readframes(audio.getnframes())))
        
        decoded_bits = [audio_array[i] & 1 for i in range(len(audio_array))]
        decoded_text = "".join(chr(int("".join(map(str, decoded_bits[i:i + 8])), 2)) for i in range(0, len(decoded_bits), 8)).split("###")[0]
        
        audio.close()
        
        messagebox.showinfo("Decoded Message", decoded_text)
    except Exception as e:
        messagebox.showerror("Error", f"Decoding Failed: {str(e)}")

# GUI Setup
root = Tk()
root.title("Audio Steganography")
root.geometry("600x400")

Label(root, text="Audio Steganography", font=("Arial", 18, "bold")).pack(pady=20)

Button(root, text="Encrypt Message", command=encode_audio, font=("Arial", 14), bg="lightblue", width=30, height=2).pack(pady=10)
Button(root, text="Decrypt Message", command=decode_audio, font=("Arial", 14), bg="lightgreen", width=30, height=2).pack(pady=10)
Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="red", width=30, height=2).pack(pady=10)

root.mainloop()
