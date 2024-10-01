import tkinter as tk
<<<<<<< HEAD

=======
>>>>>>> 330fed9e844a2c124ff1352f1fcbdc1207110cad
from tkinter import messagebox

# Encryption/Decryption Function (same for both)
def caesar_cipher(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt/Decrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

# Function to handle encryption
def encrypt_text():
    text = entry_text.get()
    try:
        s = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")
        return
    
    if s < 0 or s > 25:
        messagebox.showerror("Input Error", "Shift value must be between 0 and 25.")
        return
    
    encrypted_text = caesar_cipher(text, s)
    label_result.config(text=f"Encrypted Text: {encrypted_text}")

# Function to handle decryption
def decrypt_text():
    text = entry_text.get()
    try:
        s = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")
        return
    
    if s < 0 or s > 25:
        messagebox.showerror("Input Error", "Shift value must be between 0 and 25.")
        return
    
    decrypted_text = caesar_cipher(text, 26 - s)
    label_result.config(text=f"Decrypted Text: {decrypted_text}")

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
<<<<<<< HEAD
window.geometry("800x500")
=======
window.geometry("400x300")
>>>>>>> 330fed9e844a2c124ff1352f1fcbdc1207110cad

# Label for instructions
label_instruction = tk.Label(window, text="Enter the text and shift value for encryption/decryption:")
label_instruction.pack(pady=10)

# Text entry field
label_text = tk.Label(window, text="Text:")
label_text.pack()
entry_text = tk.Entry(window, width=40)
entry_text.pack()

# Shift value entry field
label_shift = tk.Label(window, text="Shift Value (0-25):")
label_shift.pack()
entry_shift = tk.Entry(window, width=5)
entry_shift.pack()

# Buttons for encryption and decryption
button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_text)
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_text)
button_decrypt.pack(pady=10)

# Label to display the result
label_result = tk.Label(window, text="Result will be shown here")
label_result.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()