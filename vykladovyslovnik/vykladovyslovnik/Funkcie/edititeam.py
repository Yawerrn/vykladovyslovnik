#!/usr/bin/python3
import json

def EditIteam(kluc, hodnota, data, nazslovnik):

    if not kluc in data["slovnik"]:
        print("Slovo je uz v slovniku.")
        return False
    else:
        data["slovnik"][kluc] = {}
        data["slovnik"][kluc][hodnota] = 0
        d = json.dumps(data, indent=4,ensure_ascii=False)
        with open(nazslovnik, "w", encoding='utf-8') as outfile:
            outfile.write(d)
        return True
