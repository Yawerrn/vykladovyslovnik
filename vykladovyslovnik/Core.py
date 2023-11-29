#!/usr/bin/python3

import argparse

import parseargs










'''
word = input("Zadajte slovo: ")

slovnik = {
    "auto" : "vozidlo",
    "voda" : "kvapalina",
    "kamera" : "zariadenie na nahravanie"

}

slovnik[word] = "Zadany vyraz nie je v slovniku"

print (slovnik[word])
print ("Hladane slovo je: " + word) 
'''
import json

args = parseargs.our_init_parse()

#print(args)

if not args.search is None:
    print("Search")
elif not args.delete is None:
    print("Vymazat")
elif not args.number is None:
    print("Vypisat TOP")
else:  
    exit("CHYBA - toto by sa nemalo stat")
exit()



f = open('db.json')
data = json.load(f)


vstup1 = input("Zadajte slovo: ")
vstup2 = input("Zadajte vysvetlenie: ")

data["slovnik"][vstup1] = vstup2


d = json.dumps(data, indent=4)

with open("db.json", "w") as outfile:
    outfile.write(d)



def printdic(data) :
    for x in data["slovnik"]:
        print(x + " : " + data["slovnik"][x])

kluc = input("Zadajte slovo ktore chete vymazat: ")

del data["slovnik"][kluc] 
with open('db.json', 'w') as kluc:
    json.dump(data, kluc)

printdic(data)
    
    


'''
kluc = input("Zadajte slovo: ")

 
if 'slovnik' in data and kluc in data['slovnik']:
    print("Vyznam slova " +kluc)
    print(data['slovnik'][kluc])

else :
    print("Toto slovo sa nenachazda v slovniku")


'''