#!/usr/bin/python3
import json

def DeleteIteamFromDb(kluc, data):


    if kluc in data["slovnik"]:
        del data["slovnik"][kluc]
        with open('db.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        delslovo = "Slovo bolo úspešne vymazané."
        return delslovo
    else:
        print("Slovo sa nenachádza v slovníku.")
        delslovo = "Slovo sa nenachádza v slovníku."
        return delslovo
        exit()

with open('db.json') as f:
    data = json.load(f)

