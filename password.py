import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.password_length = tk.IntVar()
        self.include_uppercase = tk.BooleanVar()
        self.include_numbers  = tk.BooleanVar()
        self.include_symbols  = tk.BooleanVar()
        self.exclude_chars = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text = "Advanced Password Generator", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text = "Password Length:").pack()
        tk.Entry(self.root, textvariable=self.password_length).pack()
        tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_uppercase).pack()
        tk.Checkbutton(self.root, text="Include Numbers", variable=self.include_numbers).pack()
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols).pack()
        tk.Label(self.root, text="Exclude Characters(optional):").pack()
        tk.Entry(self.root, textvariable=self.exclude_chars).pack()
        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)
        self.password_output = tk.Entry(self.root, font=("Arial", 12), justify='center')
        self.password_output.pack(pady=5)
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack()

    def generate_password(self):
        try:
            length = self.password_length.get()
            if length < 4:
                messagebox.showerror("Invalid Length", "Password length should be at least 4.")
                return 
            
            character_pool = list(string.ascii_lowercase)

            if self.include_uppercase.get():
                character_pool.extend(string.ascii_uppercase)

            if self.include_numbers.get():
                character_pool.extend(string.digits)

            if self.include_symbols.get():
                character_pool.extend(string.punctuation)

            exclude = self.exclude_chars.get()
            if exclude:
                character_pool = [c for c in character_pool if c not in exclude]

            if len(character_pool) == 0:
                messagebox.showerror("Invalid Characters", "Character pool is empty. Please adjust your settings.")
                return
            
            password =  ''.join(random.choice(character_pool) for _ in range(length))
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, password)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

    def copy_to_clipboard(self):
        password = self.password_output.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("No Password", "Please generate a password first.")

if __name__ == "__main__":
   root = tk.Tk()
   app = PasswordGeneratorApp(root)
   root.mainloop()








