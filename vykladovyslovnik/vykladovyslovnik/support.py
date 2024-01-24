#!/usr/bin/python3

import json

def printdic(data) :
    for x in data["slovnik"]:
        print(x + " : " + data["slovnik"][x]) 

def additeamtoDB(dbFileName):
    f = open(dbFileName)
    data = json.load(f)
    kluc = input("Zadajte slovo: ")
    hodnota = input("Zadajte vysvetlenie slova: ")
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


def searchingInDB(kluc, dbFileName) :
    f = open(dbFileName)
    data = json.load(f)
    kluc = input("Zadajte slovo: ")
    if 'slovnik' in data and kluc in data['slovnik']:
        print("Vyznam slova " +kluc)
        print(data['slovnik'][kluc])
    else :
        print("Toto slovo sa nenachazda v slovniku")

def deleteInDB(dbFileName) :
    f = open(dbFileName)
    data = json.load(f)

    kluc = input("Zadajte slovo ktore chete vymazat: ")

    del data["slovnik"][kluc] 
    with open('db.json', 'w') as kluc:
        json.dump(data, kluc)


    