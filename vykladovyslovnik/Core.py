#!/usr/bin/python3
"""
 word = input("Zadajte slovo: ")

slovnik = {
    "auto" : "vozidlo",
    "voda" : "kvapalina",
    "kamera" : "zariadenie na nahravanie"

}

slovnik[word] = "Zadany vyraz nie je v slovniku"

print (slovnik[word])
print ("Hladane slovo je: " + word) 
"""

def printdic(data) :
    for x in data["slovnik"]:
        print(x + " : " + data["slovnik"][x]) 

import json

f = open('db.json')
data = json.load(f)

vstup1 = input("Zadajte slovo: ")
vstup2 = input("Zadajte vysvetlenie: ")

data["slovnik"][vstup1] = vstup2

printdic(data)

d = json.dumps(data, indent=4)

with open("db.json", "w") as outfile:
    outfile.write(d)





