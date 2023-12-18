import tkinter as tk
from tkinter import messagebox
import json

with open('db.json') as f:
    data = json.load(f)

class MyGUI:

    def __init__(self):
        self.kluc = "" 

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Najcastejsie vyhladavane slova", font=('Arial', 18))
        self.label.pack(padx=350, pady=350)

        self.button = tk.Button(self.root, text="Vyhladaj", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        from Funkcie.topsch import TopSchf
        messagebox.showinfo(title="Message", message=TopSchf(data))
        
MyGUI()