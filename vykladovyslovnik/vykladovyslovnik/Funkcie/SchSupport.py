
def searchiteamfuncsupport(kluc, data, nazslovnik):
    if kluc in data["slovnik"]:
        hodnota = data["slovnik"][kluc]
        vysslova = next(iter(hodnota.keys()))
        print(f"Vysvetlenie slova {kluc} je {vysslova}")
        return vysslova

    else:
        print(f"Slovo '{kluc}' nie je v slovniku.")
        return None