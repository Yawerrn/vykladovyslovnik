import tkinter as tk
from tkinter import messagebox
import json

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Button Redirects")

        with open('db.json') as f:
            self.data = json.load(f)

        button_texts = ["Hladat", "Pridat", "Odstranit", "Najcastie hladane slova", "Posledne hladane slova"]
        for i, text in enumerate(button_texts):
            command = lambda idx=i: self.button_click(idx)
            button = tk.Button(self.root, text=text, font=('Arial', 34), command=command)
            button.pack(pady=50,padx=500)

        self.root.mainloop()

    def button_click(self, index):
        if index == 0:
            from GuiSearch import MyGUI
            MyGUI()
            pass
        elif index == 1:
            from GuiAdd import MyGUI
            MyGUI()
            pass
        elif index == 2:
            from GuiDelete import MyGUI
            MyGUI()
            pass
        elif index == 3:
            from GuiTopSch import MyGUI
            MyGUI()
            pass
        elif index == 4:
            from GuiLastsch import MyGUI
            MyGUI()
            pass



# Create an instance of the GUI
MyGUI()
