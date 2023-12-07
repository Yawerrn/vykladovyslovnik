#!/usr/bin/python3
import json

def vypis_poslednych_5_vyhladanych_vyrazov(data):
    print("Posledných 5 vyhľadaných výrazov sú:")
    for x in data["recent"]:
        print(x)


with open('db.json') as f:
        data = json.load(f)

vypis_poslednych_5_vyhladanych_vyrazov(data)