# Steganography-for-Audio-Image-Files
![image](https://github.com/user-attachments/assets/85ea47ab-db10-480a-aee8-cfe2ba447fa8)
Developed a steganography-based encryption tool that allows users to securely hide and retrieve secret messages within audio (.wav) and image (.jpg/.png) files. This project integrates Python, OpenCV, and Tkinter to provide a user-friendly GUI for encrypting and decrypting hidden data.

🔑 Key Features:
✅ Audio Steganography: Hide messages within WAV files using LSB encoding.
✅ Image Steganography: Embed and extract messages from JPG/PNG files.
✅ Password Protection: Ensures only authorized users can decrypt the hidden content.
✅ User-Friendly GUI: Built with Tkinter for seamless interaction.
✅ Secure Encoding & Decoding: Data is efficiently embedded without altering file integrity.

This project enhances data security and privacy protection, making it a useful tool for confidential communication. 🚀

📋 Requirements
**Ensure you have the following dependencies installed:**
Python 3.8+
OpenCV
NumPy
Tkinter (included with Python)
Wave (built-in with Python)
**Set Paths for Required Files**
Ensure that the paths for input and output files (audio/image) are correctly set within the code.
Modify file paths in main.py, audio_steg.py, and image_steg.py if necessary.


**▶️ Running the Project**
Run the main script to launch the GUI:
python main.py

This will open the application window where you can encode or decode hidden messages in audio and image files.
