import tkinter as tk
from tkinter import messagebox
import json

with open('db.json') as f:
    data = json.load(f)

root = tk.Tk()
root.geometry('1000x650')
root.title('Výkladový Slovník')

lb = None  # Initialize lb as a global variable

def search_page():
    def search():
        kluc = entry.get()
        from Funkcie.searchitem import searchiteamfunc
        messagebox.showinfo(title=kluc, message='Slovo ' + kluc + ' znamena ' + searchiteamfunc(kluc, data))
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
        kluc = entry1.get()
        vysvetlenie = entry2.get()
        from Funkcie.additem import AddIteamToDB
        AddIteamToDB(kluc, vysvetlenie, data)
        messagebox.showinfo(title=kluc, message="Slovo bolo úspešne pridané.")
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
        key = entry.get()
        from Funkcie.deleteiteam import DeleteIteamFromDb
        messagebox.showinfo(title="Message", message=DeleteIteamFromDb(key,data))
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
        from Funkcie.topsch import TopSchf
        messagebox.showinfo(title="Najčastejšie hľadané slová", message=TopSchf(data))
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
        from Funkcie.lastsch import LastSchfunc
        messagebox.showinfo(title="Posledné hľadané slová", message=LastSchfunc(data))
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

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()


options_frame = tk.Frame(root, bg='#c3c3c3')



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
options_frame.configure(width=240, height=800)


main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2 )

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=3000, width=3000)


root.mainloop()

