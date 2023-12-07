#!/usr/bin/python3
import json

with open('db.json') as f:
    data = json.load(f)

sorted_words = sorted(data["slovnik"].items(), key=lambda x: x[1]["pocet"], reverse=True)
top_5 = sorted_words[:5]
print("5 Najcastesie vyhladavanych slov je :")
for word, values in top_5:
    print(f"{word}: {values['pocet']}")
