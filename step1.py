# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:06:29 2020

@author: Leqsi
"""

from avl import AVL_Tree
import random

class Tournoi(object):
    """Tournoi class that contains an AVL_tree initialized 
    to 0 mean score and incremental ID"""
    def __init__(self):
        self.root = None
        self.mon_arbre = AVL_Tree()
        for i in range (100):
            self.root = self.mon_arbre.insert(self.root,0,i+1,0)
        
    def reset_scores(self,root):
        """Method that set score to 0 for each Node """
        if root:
            root.score_moyen = 0
            self.reset_scores(root.left)
            self.reset_scores(root.right)          
            
    def increase_games(self,root):
        """Method that increment number of games by 1 for each node"""
        if root == None:
            return root
        root.nb_games += 1
        return self.increase_games(root.left)
        return self.increase_games(root.right)
    
    def play_3game_random(self):
        """Method that play 3 random game (do not consider the score)
        that generate scores each game"""
        ar = []
        self.mon_arbre.inOrderArray(self.root,ar)
        for i in range (3):
            ar = random.sample(ar,100)
            for i in range (int(len(ar)/10)):
                players = ar[i*10:(i+1)*10]
                #print(players)
                play_game(players)
                #("DEBUG ",players)
                reset_role(players)
        self.root = None
        self.mon_arbre = AVL_Tree()
        for el in ar:
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id,el.nb_games)        
            
    def play_game_until_end(self):
        """Method that play the tournament until 10 players remaining 
        It consider the mean score"""
        ar = []
        self.mon_arbre.inOrderArray(self.root,ar)
        ar.sort(key= lambda x: x.score_moyen)
        #print(ar)
        #print(ar)
        while(len(ar)> 10):
            ar.sort(key= lambda x: x.score_moyen)
            for i in range (int(len(ar)/10)):
                players = ar[i*10:(i+1)*10]
                play_game(players)
                reset_role(players)
            #ar.sort(key= lambda x: x.score_moyen)
            ar = ar[10:]
        #print(ar)
        self.root = None
        self.mon_arbre = AVL_Tree()
        for el in ar:
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id,el.nb_games)
        
        
    def play_5_last_game(self):
        """Method that play last 5 games"""
        ar = []
        self.mon_arbre.inOrderArray(self.root,ar)
        for i in range(5):
            play_game(ar)
            reset_role(ar)
        self.root = None
        self.mon_arbre = AVL_Tree()
        for el in ar:
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id,el.nb_games)
    
    def delete_last10(self):
        for i in range (10):
            self.root = self.mon_arbre.deletemin(self.root)
            
def reset_role(players):
    """Method that set impostor boolean to false for each player"""
    for player in players:
        player.impostor = False


def play_game(players):
    """Method that randomize the score based on a random
    boolean for impostor"""
    for el in players:
        el.nb_games += 1
    impostors = random.sample(players, 2)
    for player in impostors:
        player.impostor = True
    
    for play in players:
        if play.impostor:
            play.score_moyen = round((play.score_moyen + get_score_impostor() ) / play.nb_games,2)
        else:
            play.score_moyen = round((play.score_moyen + get_score_crewmate() ) / play.nb_games,2)


def get_score_impostor():
    """Random score for impostor (max = 38)"""
    alea = random.randint(0,38)
    return alea

def get_score_crewmate():
    """Random score for crewmate (max = 12 and 2,6,7,10 are impossible)"""
    impossible = [2,6,7,10]
    alea = random.randint(0,12)
    while alea in impossible:
        alea = random.randint(0,12)
    return alea


def main_step1_no_print():
    """Main function that play the tournament without print"""
    tournoi = Tournoi()

    tournoi.play_3game_random()

    tournoi.play_game_until_end()

    

    tournoi.reset_scores(tournoi.root)
    tournoi.play_5_last_game()

    ar = []
    tournoi.mon_arbre.inOrderArray(tournoi.root,ar)
    ar.sort(key= lambda x: x.score_moyen, reverse = True)

    
    print()
    print("------ PODIUM ------")
    count = 0;
    while count < 3:
        print(ar[count])
        count+=1
        
def main_step1_print():
    """Main function that play the tournament with print details"""
    tournoi = Tournoi()

    print()

    print("--------- TOURNMAMENT BEGIN ---------")
    print()
    print("--------- 3 games random : ---------")
    print()
    tournoi.play_3game_random()
    tournoi.mon_arbre.preOrder(tournoi.root)

    print()
    print()
    print("--------- Play game until 10 players remaining: ---------")
    print()
    tournoi.play_game_until_end()
    tournoi.mon_arbre.preOrder(tournoi.root)
    
    print()
    print()
    print("------ TOP 10 PLAYERS ------")
    print()
    tournoi.reset_scores(tournoi.root)
    tournoi.play_5_last_game()
    ar = []
    tournoi.mon_arbre.inOrderArray(tournoi.root,ar)
    ar.sort(key= lambda x: x.score_moyen, reverse = True)
    print(ar)
    
    print()
    print("------ PODIUM ------")
    print()
    count = 0;
    while count < 3:
        print(ar[count])
        count+=1
    

if __name__ == "__main__":
    main_step1_print()