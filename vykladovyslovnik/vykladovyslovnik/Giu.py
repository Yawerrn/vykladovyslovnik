import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import json


root = tk.Tk()
root.geometry('1000x650')
root.title('Výkladový Slovník')

lb = None  # Initialize lb as a global variable

global data1,data2

data1 = None
data2 = None

def chose_page():

    def off1():
        global data1
        toggle_photo1.configure(file='toggle-buttonoff.png')
        toggle_button1.configure(command=on1)
        data1 = None

    def on1():
        global data1,nazslovnik1
        toggle_photo1.configure(file='toggle-button.png')
        toggle_button1.configure(command=off1)

        with open('db1.json') as f:
            data1 = json.load(f)
            nazslovnik1 = "db1.json"

    def off2():
        global data2
        toggle_photo2.configure(file='toggle-buttonoff.png')
        toggle_button2.configure(command=on2)
        data2 = None

    def on2():
        global data2, nazslovnik2
        toggle_photo2.configure(file='toggle-button.png')
        toggle_button2.configure(command=off2)
        with open('db2.json') as f:
            data2 = json.load(f)
            nazslovnik2 = "db2.json"

    global chk_var, label_var

    chose_frame = tk.Frame(main_frame)


    toggle_photo1 = PhotoImage(file='toggle-buttonoff.png')
    toggle_button1 = Button(root, image=toggle_photo1,border=0,command=off1)
    toggle_button1.place(x=250,y=70)


    toggle_photo2 = PhotoImage(file='toggle-buttonoff.png')
    toggle_button2 = Button(root, image=toggle_photo2,border=0,command=off2)
    toggle_button2.place(x=250,y=370)

    lb = tk.Label(chose_frame, text='Krátky slovník slovenského jazyka', font=('Bold', 25), anchor=E)
    lb.pack()


    chose_frame.pack(pady=25)


def search_page():

    def search():
        if not data1 is None:
            global kluc
            kluc = entry.get()
            from Funkcie.searchitem import searchiteamfunc
            data = data1
            nazslovnik = "db1.json"
            print(searchiteamfunc(kluc, data, nazslovnik))
            print(searchiteamfunc(kluc, data, nazslovnik) == None)
            if not searchiteamfunc(kluc, data, nazslovnik) is None:
                messagebox.showinfo(title=kluc, message=searchiteamfunc(kluc, data, nazslovnik))
                lb.pack()
                return

        if not data2 is None:
            kluc = entry.get()
            from Funkcie.searchitem import searchiteamfunc
            data = data2
            nazslovnik = "db2.json"
            print(searchiteamfunc(kluc, data, nazslovnik))
            print(searchiteamfunc(kluc, data, nazslovnik) == None)
            if not searchiteamfunc(kluc, data, nazslovnik) is None:
                messagebox.showinfo(title=kluc, message=searchiteamfunc(kluc, data, nazslovnik))
                lb.pack()
                return

        if not data1 and data2 is None:
            messagebox.showinfo(title="neni", message="vsak ale daj databzu")
            lb.pack()

        kluc = entry.get()
        if not kluc is None:
            messagebox.showinfo(title="neni", message="neni ani v jednom")
            lb.pack()



    global lb
    search_frame = tk.Frame(main_frame)

    lb = tk.Label(search_frame, text='Zadajte slovo ktore chete vyhladat', font=('Bold', 25))
    lb.pack()

    entry = tk.Entry(search_frame, font=('Bold', 20), width=30)
    entry.pack(pady=40)

    button = tk.Button(search_frame, text="Vyhľadaj", font=('Arial', 18), command=search)
    button.pack(pady=100)

    search_frame.pack(pady=25)

def add_page():

    def add():


        if data1 and data2:
            messagebox.showinfo(title="chyba", message="musis mat zapnuty max 1 slovnik.")
            lb.pack()
        elif not data1 is None:
            kluc = entry1.get()
            hodnota = entry2.get()
            data = data1
            nazslovnik = "db1.json"
            from Funkcie.additem import AddIteamToDB
            AddIteamToDB(kluc, hodnota, data, nazslovnik)
            messagebox.showinfo(title=kluc, message="Slovo bolo úspešne pridané.")
            lb.pack()
        elif not data2 is None:
            kluc = entry1.get()
            hodnota = entry2.get()
            data = data2
            nazslovnik = "db2.json"
            from Funkcie.additem import AddIteamToDB
            AddIteamToDB(kluc, hodnota, data, nazslovnik)
            messagebox.showinfo(title=kluc, message="Slovo bolo úspešne pridané.")
            lb.pack()
        else:
            messagebox.showinfo(title="chyba", message="zapnite si aspon jeden slovnik.")
            lb.pack()



    global lb
    add_frame = tk.Frame(main_frame)

    lb = tk.Label(add_frame, text='Zadajte slovo, ktoré chcete pridať', font=('Bold', 25))
    lb.pack()

    entry1 = tk.Entry(add_frame, font=('Bold', 20), width=30)
    entry1.pack(pady=30)

    lb = tk.Label(add_frame, text='Zadajte vysvetlenie slova, ktoré chcete pridať', font=('Bold', 25))
    lb.pack(pady=50)

    entry2 = tk.Entry(add_frame, font=('Bold', 20), width=30)
    entry2.pack(pady=30)

    button = tk.Button(add_frame, text="Pridaj", font=('Arial', 18), command=add)
    button.pack(pady=80)

    add_frame.pack(pady=25)


def delete_page():
    def delete():
        if data1 and data2:
            messagebox.showinfo(title="chyba", message="musis mat zapnuty max 1 slovnik.")
            lb.pack()
        elif not data1 is None:
            kluc = entry.get()
            data = data1
            nazslovnik = "db1.json"
            from Funkcie.deleteiteam import DeleteIteamFromDb
            DeleteIteamFromDb(kluc, data, nazslovnik)
            messagebox.showinfo(title=kluc, message="Slovo bolo úspešne vymazane.")
            lb.pack()
        elif not data2 is None:
            kluc = entry.get()
            data = data2
            nazslovnik = "db2.json"
            from Funkcie.deleteiteam import DeleteIteamFromDb
            DeleteIteamFromDb(kluc, data, nazslovnik)
            messagebox.showinfo(title=kluc, message="Slovo bolo úspešne vymazane.")
            lb.pack()
        else:
            messagebox.showinfo(title="chyba", message="zapnite si aspon jeden slovnik.")
            lb.pack()

    delete_frame = tk.Frame(main_frame)

    lb = tk.Label(delete_frame, text='Zadajte slovo ktore chete vymazať', font=('Bold', 25))
    lb.pack(pady=50)

    entry = tk.Entry(delete_frame, font=('Bold', 20), width=30)
    entry.pack(pady=40)

    button = tk.Button(delete_frame, text="Vymazať", font=('Arial', 18), command=delete)
    button.pack(pady=100)

    delete_frame.pack(pady=25)


def top_page():
    def top():
        if data1 and data2:
            messagebox.showinfo(title="chyba", message="musis mat zapnuty max 1 slovnik.")
            lb.pack()
        elif not data1 is None:
            from Funkcie.topsch import TopSchf
            data = data1
            messagebox.showinfo(title="Najčastejšie hľadané slová", message=TopSchf(data))
            lb.pack()
        elif not data2 is None:
            from Funkcie.topsch import TopSchf
            data = data2
            messagebox.showinfo(title="Najčastejšie hľadané slová", message=TopSchf(data))
            lb.pack()
        else:
            messagebox.showinfo(title="chyba", message="zapnite si aspon jeden slovnik.")
            lb.pack()

    global lb
    top_frame = tk.Frame(main_frame)

    lb = tk.Label(top_frame, text='Vyhľadaj najčastejšie hľadané slová.', font=('Bold', 25))
    lb.pack()

    button = tk.Button(top_frame, text="Vyhľadaj", font=('Arial', 18), command=top)
    button.pack(pady=100)

    top_frame.pack(pady=25)



def last_page():
    def last():
        if data1 and data2:
            messagebox.showinfo(title="chyba", message="musis mat zapnuty max 1 slovnik.")
            lb.pack()
        elif not data1 is None:
            data = data1
            from Funkcie.lastsch import LastSchfunc
            messagebox.showinfo(title="Posledné hľadané slová", message=LastSchfunc(data))
            lb.pack()
        elif not data2 is None:
            data = data2
            from Funkcie.lastsch import LastSchfunc
            messagebox.showinfo(title="Posledné hľadané slová", message=LastSchfunc(data))
            lb.pack()
        else:
            messagebox.showinfo(title="chyba", message="zapnite si aspon jeden slovnik.")
            lb.pack()

    global lb
    last_frame = tk.Frame(main_frame)

    lb = tk.Label(last_frame, text='Vyhľadaj posledné hľadané slová.', font=('Bold', 25))
    lb.pack()

    button = tk.Button(last_frame, text="Vyhľadaj", font=('Arial', 18), command=last)
    button.pack(pady=100)

    last_frame.pack(pady=25)


def hide_indicators():
    search_indicate.config(bg='#c3c3c3')
    add_indicate.config(bg='#c3c3c3')
    delete_indicate.config(bg='#c3c3c3')
    top_indicate.config(bg='#c3c3c3')
    last_indicate.config(bg='#c3c3c3')
    chose_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()


options_frame = tk.Frame(root, bg='#c3c3c3')


Search_btn = tk.Button(options_frame, text='Výber', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(chose_indicate,chose_page))

Search_btn.place(x=25, y=0, )

chose_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
chose_indicate.place(x=25, y=10, width=5, height=40)



Search_btn = tk.Button(options_frame, text='Hladať', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(search_indicate,search_page))

Search_btn.place(x=25, y=80, )

search_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
search_indicate.place(x=25, y=90, width=5, height=40)



add_btn = tk.Button(options_frame, text='Pridať', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(add_indicate, add_page))

add_btn.place(x=25, y=180)

add_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
add_indicate.place(x=25, y=190, width=5, height=40)


delete_btn = tk.Button(options_frame, text='Odstraniť', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(delete_indicate, delete_page))

delete_btn.place(x=25, y=280)

delete_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
delete_indicate.place(x=25, y=290, width=5, height=40)


top_btn = tk.Button(options_frame, text='Najčastejšie', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(top_indicate, top_page))

top_btn.place(x=25, y=380)

top_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
top_indicate.place(x=25, y=390, width=5, height=40)


last_btn = tk.Button(options_frame, text='Posledné', font=('Bold', 25), fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda: indicate(last_indicate, last_page))

last_btn.place(x=25, y=480)

last_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
last_indicate.place(x=25, y=490, width=5, height=40)



options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=240, height=3000)


main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2 )

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=3000, width=3000)


root.mainloop()

