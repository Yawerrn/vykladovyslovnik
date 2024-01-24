#!/usr/bin/python3
import json

def EditIteam(kluc, hodnota, data, nazslovnik):

    if not kluc in data["slovnik"]:
        print("Slovo je uz v slovniku.")
        return False
    else:
        data["slovnik"][kluc] = {}
        data["slovnik"][kluc][hodnota] = 0
        d = json.dumps(data, indent=4)
        with open(nazslovnik, "w") as outfile:
            outfile.write(d)
        return True
