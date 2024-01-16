#!/usr/bin/python3
import json

with open('db.json') as f:
    data = json.load(f)


def TopSchf(data):
    sorted_words = sorted(data["slovnik"].items(), key=lambda x: x[1]["pocet"], reverse=True)
    top_5 = sorted_words[:5]

    vysledok = []
    for word, values in top_5:
        vysledok.append(f"{word}: {values['pocet']}")  # Include the count in the message

    return '\n'.join(vysledok)

TopSchf(data)

