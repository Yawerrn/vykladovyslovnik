#!/usr/bin/python3
import json

def LastSchfunc(data):
    recent_values = data["recent"]
    result = []

    for word in recent_values:
        result.append(f"{word}")

    return '\n'.join(result)

with open('db.json') as f:
    data = json.load(f)
