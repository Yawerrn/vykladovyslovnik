#!/usr/bin/python3

import json

def printdic(data) :
    for x in data["slovnik"]:
        print(x + " : " + data["slovnik"][x]) 

def additeamtoDB(kluc, hodnota, dbFileName):
    f = open(dbFileName)
    data = json.load(f)
    data["slovnik"][kluc] = hodnota
    d = json.dumps(data, indent=4)
    with open("db.json", "w") as outfile:
        outfile.write(d)

'''
f = open('db.json')
data = json.load(f)

vstup1 = input("Zadajte slovo: ")
vstup2 = input("Zadajte vysvetlenie: ")

'''

