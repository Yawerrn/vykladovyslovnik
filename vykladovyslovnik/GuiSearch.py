import tkinter as tk
from tkinter import messagebox
import json

with open('db.json') as f:
    data = json.load(f)

class MyGUI:

    def __init__(self):
        self.kluc = "" 

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Zadajte slovo ktore chete vyhladat", font=('Arial', 18))
        self.label.pack(padx=100, pady=100)

        self.textbox = tk.Text(self.root, height=2, font=('Arial', 18))
        self.textbox.pack(padx=150, pady=100)

        self.textbox.bind('<KeyRelease>', self.update_kluc)

        self.button = tk.Button(self.root, text="Vyhladaj", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def update_kluc(self, event):
        self.kluc = self.textbox.get('1.0', tk.END)

    def show_message(self):
        key = self.kluc.strip()
        from Funkcie.searchitem import searchiteamfunc
        messagebox.showinfo(title=key, message=searchiteamfunc(key, data))
        
MyGUI()
