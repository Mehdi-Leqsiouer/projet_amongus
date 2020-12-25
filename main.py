# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:11:48 2020

@author: Leqsi
"""
from step1 import main_step1_no_print,main_step1_print
from step2 import main_step2
from step3 import step3_3,step3_4
from step4 import main_step4
from graphe import creer_graphe

def boucle():  
    """Main loop of the program """
    while True:
        print()
        print ("--------------- MENU ---------------")
        print ("--------------- Choice 1 : Step 1 : play the tournament ---------------")
        print ("--------------- Choice 2 : Step 2 : get set of impostor ---------------")
        print ("--------------- Choice 3 : Step 3 : Get shortest paths of the map ---------------")
        print ("--------------- Choice 4 : Step 4 : Get the path to go to each room only one time ---------------")
        print ("--------------- Choice 5 : Print all the vertices names (ADSA MAP : room names) ---------------")
        print ("--------------- Press : 'Q' or 'q' to leave the menu ---------------")
        print()
        reponse = str(input("Choose the step to execute : "))
        print()
        if (reponse == 'Q' or reponse == 'q'):
            break
        if (int(reponse) == 1):
            while True:
                print ("--------------- STEP 1 ---------------")
                print ("--------------- Choice 1 : Play the tournament without details (only print the result podium) ---------------")
                print ("--------------- Choice 2 : Play the tournament with details (print the tournament details)  ---------------")
                print ("--------------- Press : 'Q' or 'q' to go back to main menu ---------------")
                reponse3= str(input("Choose the method to execute : "))
                if(reponse3 == 'Q' or reponse3 == 'q'):
                    break
                elif (int(reponse3) == 1):
                    main_step1_no_print()
                elif(int(reponse3) == 2):
                    main_step1_print()
                print()
        elif (int(reponse) == 2):
            player_dead = str(input("Enter the player who died : ")).capitalize()
            main_step2(player_dead)
        elif(int(reponse) == 3):
            while True:
                print ("--------------- STEP 3 ---------------")
                print ("--------------- Choice 1 : Pathfinding between 2 vertex (crewmate and impostor) ---------------")
                print ("--------------- Choice 2 : Interval of time for EACH PAIR of rooms as impostor ---------------")
                print ("--------------- Press : 'Q' or 'q' to go back to main menu ---------------")
                reponse2 = str(input("Choose the method to execute : "))
                if (reponse2 == 'Q' or reponse2 == 'q'):
                    break
                elif (int(reponse2) == 1):                
                    depart  = str(input("Enter the starting vertex : "))
                    arriver = str(input("Enter the ending vertex :  "))
                    depart = clean_input(depart)
                    arriver = clean_input(arriver)
                    step3_3(depart,arriver)                   
                elif(int(reponse2) == 2):
                    step3_4()   
                print()
        elif(int(reponse) == 4):
            main_step4()
            
        elif (int(reponse) == 5):
            g = creer_graphe("step4.dat")
            sommets = g.keys()
            for el in sommets:
                print(el,end=" -- ")
        print()


def clean_input(input_string):
    """Method that clean input (capitalize considering '_' char) """
    if '_' in input_string:
        dep1 = input_string.split('_')
        newstring1 = ''
        for el in dep1:
            newstring1 += el.capitalize()+'_'
        input_string = newstring1[0:len(newstring1)-1]
    else:
        input_string = input_string.capitalize()
    return input_string

if __name__ == "__main__":
    boucle()