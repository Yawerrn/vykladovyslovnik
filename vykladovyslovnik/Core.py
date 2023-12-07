#!/usr/bin/python3
import argparse

import parseargs

import json

with open('db.json') as f:
    data = json.load(f)

args = parseargs.our_init_parse()

if not args.search is None:
    print("Search")
    from Funkcie.searchitem import searchiteamfunc
    prosim = searchiteamfunc(args.search, data)
    print(prosim)
elif not args.delete is None:
    print("Vymazat")
    from Funkcie.deleteiteam import deleteiteamfunc
    deleteiteamfunc(args.delete, data)
    
elif not args.add is None:
    print("Vypisat TOP")
elif not args.last is None:
    print("Vypisat TOP")
else:  
    exit("CHYBA - toto by sa nemalo stat")
exit()

"""
def printdic(data) :
    for x in data["slovnik"]:
        print(x + " : " + data["slovnik"][x])
"""