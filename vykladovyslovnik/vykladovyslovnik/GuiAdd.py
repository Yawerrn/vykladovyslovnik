import tkinter as tk
from tkinter import messagebox
import json

with open('db.json') as f:
    data = json.load(f)

class MyGUI:

    def __init__(self):
        self.kluc = ""
        self.vysvetlenie = ""

        self.root = tk.Tk()

        self.label1 = tk.Label(self.root, text="Zadajte slovo ktore chete pridat", font=('Arial', 18))
        self.label1.pack(padx=25, pady=25)

        self.textbox1 = tk.Text(self.root, height=2, font=('Arial', 18))
        self.textbox1.pack(padx=150, pady=50)

        self.label2 = tk.Label(self.root, text="Zadajte vysvetlenia slovo", font=('Arial', 18))
        self.label2.pack(padx=25, pady=25)

        self.textbox2 = tk.Text(self.root, height=2, font=('Arial', 18))
        self.textbox2.pack(padx=150, pady=50)

        self.textbox1.bind('<KeyRelease>', self.update_kluc)
        self.textbox2.bind('<KeyRelease>', self.update_kluc)

        self.button = tk.Button(self.root, text="Pridaj", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def update_kluc(self, event):
        self.kluc = self.textbox1.get('1.0', tk.END).strip()
        self.vysvetlenie = self.textbox2.get('1.0', tk.END).strip()

    def show_message(self):
        kluc = self.kluc.strip()
        vysvetlenie = self.vysvetlenie.strip()
        from Funkcie.additem import AddIteamToDB
        AddIteamToDB(kluc, vysvetlenie, data)
        messagebox.showinfo(title="Message", message="Slovo bolo uspesne pridane")

MyGUI()
