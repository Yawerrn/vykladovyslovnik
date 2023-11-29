#!/usr/bin/python3

import json

with open('db.json') as f:
    data = json.load(f)

kluc = input("Zadajte slovo ktore chete vymazat: ")

del data["slovnik"][kluc] 
with open('db.json', 'w') as kluc:
    json.dump(data, kluc, indent=4)