#!/usr/bin/python3

import json

f = open('db.json')
data = json.load(f)

kluc = input("Zadajte slovo: ")
hodnota = input("Zadajte vysvetlenie slova: ")

if kluc not in data["slovnik"]:
    data["slovnik"][kluc] = {}

data["slovnik"][kluc][hodnota] = 0


d = json.dumps(data, indent=4)
with open("db.json", "w") as outfile:
    outfile.write(d)

data["slovnik"][kluc]["pocet"] = 0


d = json.dumps(data, indent=4)
with open("db.json", "w") as outfile:
    outfile.write(d)

