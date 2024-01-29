import json


def AddIteamToDB(kluc, hodnota, data, nazslovnik):
    if kluc in data["slovnik"]:
        print("Slovo je uz v slovniku.")
        return False
    else:
        data["slovnik"][kluc] = {}
        data["slovnik"][kluc][hodnota] = 0
        data["slovnik"][kluc]["pocet"] = 0

        d = json.dumps(data, indent=4,ensure_ascii=False)
        with open(nazslovnik, "w", encoding='utf-8') as outfile:
            outfile.write(d)

        return True