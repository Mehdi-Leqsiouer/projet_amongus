# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:06:29 2020

@author: Leqsi
"""

from avl import AVL_Tree
import random
import drawtree

class Tournoi(object):
    
    def __init__(self):
        self.root = None
        self.mon_arbre = AVL_Tree()
        for i in range (100):
            self.root = self.mon_arbre.insert(self.root,0,i+1,0)
        
    def reset_scores(self,root):
        if root:
            root.score_moyen = 0
            self.reset_scores(root.left)
            self.reset_scores(root.right)          
            
    def increase_games(self,root):
        if root == None:
            return root
        root.nb_games += 1
        return self.increase_games(root.left)
        return self.increase_games(root.right)
    
    def play_3game_random(self):
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
            
    def play_3game_random_bis(self):
        for i in range(3):
            list_impostor = []
            r = random.randint(1,100)
            for i in range(20):
                while r in list_impostor:
                    r = random.randint(1,100)
                list_impostor.append(r)      
            #self.root = self.increase_games(self.root)        
            self.update_score_tree(self.root,list_impostor)
        
        
  
    def re_create_tree(self,root):
        pass     
        
            
    def update_score_tree(self,root,list_impostor):
        if root:
            #root.nb_games += 1
            nb_g = root.nb_games + 1
            l_id = root.id
            score = root.score_moyen
            #print(root)
            if l_id in list_impostor:
                new_score = round((score + get_score_impostor() ) / nb_g,3)
                self.root = self.mon_arbre.changeKey(self.root,score,new_score,l_id,nb_g)
                list_impostor.remove(l_id)
            else:
                new_score = round((score + get_score_crewmate() ) / nb_g,3)
                self.root = self.mon_arbre.changeKey(self.root,score,new_score,l_id,nb_g)
            self.update_score_tree(root.left,list_impostor)
            self.update_score_tree(root.right,list_impostor)
            
    def play_game_until_end(self):
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
    for player in players:
        player.impostor = False


def play_game(players):
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
    alea = random.randint(0,38)
    return alea

def get_score_crewmate():
    impossible = [2,6,7,10]
    alea = random.randint(0,12)
    while alea in impossible:
        alea = random.randint(0,12)
    return alea


def main_step1():
    tournoi = Tournoi()
    tournoi.mon_arbre.preOrder(tournoi.root)
    #drawtree(tournoi.root)
    #tournoi.delete_last10()
    print()
    print("Delete")
    #tournoi.mon_arbre.preOrder(tournoi.root)
    print()
    #t = tournoi.mon_arbre.randomNode(tournoi.root,tournoi.mon_arbre.size(tournoi.root))
    #print(t)
    tournoi.play_3game_random()
    tournoi.mon_arbre.preOrder(tournoi.root)
    #drawtree(tournoi.root)
    print()
    print()
    tournoi.play_game_until_end()
    tournoi.mon_arbre.preOrder(tournoi.root)
    
    print()
    print()
    print("------ TOP 10 PLAYERS ------")
    tournoi.reset_scores(tournoi.root)
    tournoi.play_5_last_game()
    #tournoi.mon_arbre.inOrder(tournoi.root)
    ar = []
    tournoi.mon_arbre.inOrderArray(tournoi.root,ar)
    ar.sort(key= lambda x: x.score_moyen, reverse = True)
    print(ar)
    
    print()
    print("------ PODIUM ------")
    count = 0;
    while count < 3:
        print(ar[count])
        count+=1
        
   # drawtree(tournoi.root)
    

    """tournoi.mon_arbre.inOrder(tournoi.root)
    #tournoi.root = tournoi.mon_arbre.delete(tournoi.root,0)
    
    #tournoi.root = tournoi.mon_arbre.changeKey(tournoi.root,0,10,1,1)
    tournoi.play_3game_random_bis()
    #tournoi.mon_arbre.inOrder(tournoi.root)
    print()
    print()
    #print(tournoi.mon_arbre.getMinValueNode(tournoi.root))
    tournoi.mon_arbre.inOrder(tournoi.root)
    #drawtree(tournoi.root)"""
   
    
        

if __name__ == "__main__":
    main_step1()