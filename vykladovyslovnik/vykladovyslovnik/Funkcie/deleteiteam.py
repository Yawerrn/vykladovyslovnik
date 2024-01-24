#!/usr/bin/python3
import json

def DeleteIteamFromDb(kluc, data, nazslovnik):


    if kluc in data["slovnik"]:
        del data["slovnik"][kluc]
        with open(nazslovnik, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        return True
    else:
        print("Slovo sa nenachádza v slovníku.")
        return False

