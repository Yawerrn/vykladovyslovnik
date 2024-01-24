#!/usr/bin/python3
import json

def AddIteamToDB(kluc, hodnota, data, nazslovnik):

    if kluc in data["slovnik"]:
        print("Slovo je uz v slovniku.")
        return False
    else:
        data["slovnik"][kluc] = {}
        data["slovnik"][kluc][hodnota] = 0
        d = json.dumps(data, indent=4)
        with open(nazslovnik, "w") as outfile:
            outfile.write(d)
        data["slovnik"][kluc]["pocet"] = 0
        d = json.dumps(data, indent=4)
        with open(nazslovnik, "w") as outfile:
            outfile.write(d)
        return True
'''
f = open('db.json')
data = json.load(f)

kluc = input("Zadajte slovo: ")
hodnota = input("Zadajte vysvetlenie slova: ")

AddIteamToDB(kluc, hodnota, data)
'''