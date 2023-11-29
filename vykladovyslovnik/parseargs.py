#!/usr/bin/python3


import argparse

def our_init_parse():
    parser = argparse.ArgumentParser(
                        prog='Vykladovy slovnik',
                        description='Co by to asi robilo, no vyklada to slovaa',
                        epilog='Uzivatel pouzivanim tohto nastroja suhlasi s dodrziavanim bezpecnostnych smernic OSN a NATO a viaze sa k konaniu takemu, ktore bude v sulade s ludskymi pravami a zaujmami.')


    parser.add_argument('-s', '--search')      # option that takes a value
    parser.add_argument('-d', '--delete')      # option that takes a value
    parser.add_argument('-t', '--number')      # option that takes a value



    args = parser.parse_args()
    return args


     # /bin/python3 /home/yawerrn/vykladovyslovnik/Core.py -d "voda" -t 5
     # ./Core.py -d "voda" -t 5

