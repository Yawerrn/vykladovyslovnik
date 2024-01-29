#!/usr/bin/python3
import json

def searchiteamfunc(kluc, data, nazslovnik):
    if kluc in data["slovnik"]:
        hodnota = data["slovnik"][kluc]
        vysslova = next(iter(hodnota.keys()))
        print(f"Vysvetlenie slova {kluc} je {vysslova}")
        ink = hodnota.get("pocet", 0)
        ink += 1
        hodnota["pocet"] = ink

        if "recent" not in data:
            data["recent"] = []
        data["recent"].insert(0, kluc)
        if len(data["recent"]) > 5:
            data["recent"] = data["recent"][:5]

        d = json.dumps(data, indent=4,ensure_ascii=False)
        with open(nazslovnik, "w", encoding='utf-8') as outfile:
            outfile.write(d)
        return vysslova

    else:
        print(f"Slovo '{kluc}' nie je v slovniku.")
        return None