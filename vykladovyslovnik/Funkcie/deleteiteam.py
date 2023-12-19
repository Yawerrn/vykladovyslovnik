#!/usr/bin/python3
import json

def DeleteIteamFromDb(kluc, data):


    if kluc in data["slovnik"]:
        del data["slovnik"][kluc]
        with open('db.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print("Slovo sa nenachádza v slovníku.")
        exit()

with open('db.json') as f:
    data = json.load(f)

