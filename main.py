# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:30:20 2020

@author: mleqsiouer
"""

import random
# --- Step 1: To organize the tournament ---



def random_score_crewmate():
    impossible = [2,6,7,10]
    alea = random.randint(0,12)
    while alea in impossible:
        alea = random.randint(0,12)
    return alea


def random_score_impostor():
    #impossible = [28,29,30,31,32,33,34,35,36,37]
    alea = random.randint(0,12)
    #while alea in impossible:
    alea = random.randint(0,38)
    return alea


def main():
    alea = random_score_crewmate()
    print(alea)
    alea2 = random_score_impostor()
    print(alea2)

if __name__ == "__main__":    
    main()