# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:11:48 2020

@author: Leqsi
"""
from step1 import main_step1
from step2 import main_step2
from step3 import main_step3
from step4 import main_step4

def boucle():  
    while True:
        print()
        print ("--------------- MENU ---------------")
        print ("--------------- Choice 1 : Step 1 : play the tournament ---------------")
        print ("--------------- Choice 2 : Step 2 : get set of impostor ---------------")
        print ("--------------- Choice 3 : Step 3 : Get shortest paths of the map ---------------")
        print ("--------------- Choice 4 : Step 4 : Get the path to go to each room only one time ---------------")
        print ("--------------- Press : 'Q' or 'q' to leave the menu ---------------")
        print()
        reponse = str(input("Choose the step to execute : "))
        print()
        if (reponse == 'Q' or reponse == 'q'):
            break
        if (int(reponse) == 1):
            main_step1()
        elif (int(reponse) == 2):
            player_dead = str(input("Enter the player who died : "))
            main_step2(player_dead)
        elif(int(reponse) == 3):
            depart  = str(input("Enter the starting vertex : "))
            arriver = str(input("Enter the ending vertex :  "))
            main_step3(depart,arriver)
        elif(int(reponse) == 4):
            main_step4()


if __name__ == "__main__":
    boucle()