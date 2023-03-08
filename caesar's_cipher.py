import tkinter as tk

FONT = ("calbri", 15, "bold")


# Encrypt the plaintext using the key
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():                                        # if the character is a letter
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)   # shift the letter by the key
        else:
            ciphertext += char
    return ciphertext


# Decrypt the ciphertext using the key
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            plaintext += char
    return plaintext


# Create the GUI
class CaesarCipherGUI:
    def __init__(self, master):
        master.title("Caesar Cipher")

        # Create a new frame
        self.frame = tk.Frame(master)
        self.frame.pack(padx=5, pady=5)
        self.frame.configure(background='lightblue')

        # Create variables
        self.plaintext = tk.StringVar(value="")                     # plaintext is the message to be encrypted
        self.ciphertext = tk.StringVar(value="")                    # ciphertext is the encrypted message
        self.key = tk.IntVar()                                      # key is the number of letters to shift

        # Plaintext controls
        self.plain_label = tk.Label(self.frame, text="Plaintext", fg="green", font=FONT, bg='lightblue')
        self.plain_label.grid(row=0, column=0)
        self.plain_entry = tk.Entry(self.frame,textvariable=self.plaintext, width=50, font=FONT, bg='lightblue', fg='black')
        self.plain_entry.grid(row=0, column=1, padx=20)

        # Encrypt button
        self.encrypt_button = tk.Button(self.frame, text="Encrypt", command=lambda: self.encrypt_callback(), font=FONT, bg='blue', fg='black')
        self.encrypt_button.grid(row=0, column=2)
        self.plain_clear = tk.Button(self.frame, text="Clear", command=lambda: self.clear('plain'), font=FONT, bg='blue', fg='black')
        self.plain_clear.grid(row=0, column=3)

        # Key controls
        self.key_label = tk.Label(self.frame, text="Key", font=FONT, bg='lightblue')
        self.key_label.grid(row=1, column=0)
        self.key_entry = tk.Entry(self.frame, textvariable=self.key, width=10, font=FONT, bg='lightblue', fg='black')
        self.key_entry.grid(row=1, column=1, sticky=tk.W, padx=20)

        # Ciphertext controls
        self.cipher_label = tk.Label(self.frame, text="Ciphertext", fg="black", font=FONT, bg='lightblue')
        self.cipher_label.grid(row=2, column=0)
        self.cipher_entry = tk.Entry(self.frame, textvariable=self.ciphertext, width=50, font=FONT, bg='lightblue', fg='black')
        self.cipher_entry.grid(row=2, column=1, padx=20)
        self.decrypt_button = tk.Button(self.frame, text="Decrypt", command=lambda: self.decrypt_callback(), font=FONT, bg='blue', fg='black')
        self.decrypt_button.grid(row=2, column=2)
        self.cipher_clear = tk.Button(self.frame, text="Clear", command=lambda: self.clear('cipher'), font=FONT, fg='black')
        self.cipher_clear.grid(row=2, column=3)


    # Clear the entry fields
    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')

    # Get the key value
    def get_key(self):
        try:
            key_val = self.key.get()
            return key_val
        except tk.TclError:
            pass

    # Encrypt the plaintext
    def encrypt_callback(self):
        key = self.get_key()
        if key is None:
            tk.messagebox.showerror("Error", "Invalid key entered")
        else:
            ciphertext = encrypt(self.plain_entry.get(), key)
            self.cipher_entry.delete(0, tk.END)                          # Delete the current contents of the entry field
            self.cipher_entry.insert(0, ciphertext)                      # Insert the new ciphertext

    # Decrypt the ciphertext
    def decrypt_callback(self):
        key = self.get_key()                                             # Get the key value
        if key is None:
            tk.messagebox.showerror("Error", "Invalid key entered")
        else:
            plaintext = decrypt(self.cipher_entry.get(), key)
            self.cipher_entry.delete(0, tk.END)
            self.cipher_entry.insert(0, plaintext)



if __name__ == "__main__":
    root = tk.Tk()
    caesar = CaesarCipherGUI(root)
    root.mainloop()










