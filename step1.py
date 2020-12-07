# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:06:29 2020

@author: Leqsi
"""

from avl import AVL_Tree
import random

class Tournoi(object):
    
    def __init__(self):
        self.root = None
        self.mon_arbre = AVL_Tree()
        for i in range (100):
            self.root = self.mon_arbre.insert(self.root,0,i+1)
        
    def reset_scores(self,root):
        if root:
            root.score_moyen = 0
            self.reset_scores(root.left)
            self.reset_scores(root.right)
            
    def play_3game_random(self):
        ar = []
        self.mon_arbre.inOrderArray(self.root,ar)
        for i in range (3):
            ar = random.sample(ar,100)
            for i in range (int(len(ar)/10)):
                players = ar[i*10:(i+1)*10]
                #print(players)
                play_game(players)
                reset_role(players)
        #print(ar)
        self.root = None
        self.mon_arbre = AVL_Tree()
        for el in ar:
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id)
            
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
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id)
        
        
    def play_5_last_game(self):
        ar = []
        self.mon_arbre.inOrderArray(self.root,ar)
        for i in range(5):
            play_game(ar)
            reset_role(ar)
        self.root = None
        self.mon_arbre = AVL_Tree()
        for el in ar:
            self.root = self.mon_arbre.insert(self.root,el.score_moyen,el.id)
    
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
    #impossible = [28,29,30,31,32,33,34,35,36,37]
    alea = random.randint(0,12)
    #while alea in impossible:
    alea = random.randint(0,38)
    return alea

def get_score_crewmate():
    impossible = [2,6,7,10]
    alea = random.randint(0,12)
    while alea in impossible:
        alea = random.randint(0,12)
    return alea



def drawtree(root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1
        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y-20)
                t.write(node.score_moyen, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x-dx, y-60, dx/2)
                jumpto(x, y-20)
                draw(node.right, x+dx, y-60, dx/2)
        import turtle
        t = turtle.Turtle()
        t.speed(0); turtle.delay(0)
        h = height(root)
        jumpto(0, 30*h)
        draw(root, 0, 30*h, 40*h)
        t.hideturtle()
        turtle.mainloop()
            



def main():
    tournoi = Tournoi()
    tournoi.mon_arbre.preOrder(tournoi.root)
    #drawtree(tournoi.root)
    #tournoi.delete_last10()
    print()
    print("Delete")
    #tournoi.mon_arbre.preOrder(tournoi.root)
    print()
    t = tournoi.mon_arbre.randomNode(tournoi.root,tournoi.mon_arbre.size(tournoi.root))
    print(t)
    tournoi.play_3game_random()
    tournoi.mon_arbre.preOrder(tournoi.root)
    #drawtree(tournoi.root)
    print()
    print()
    tournoi.play_game_until_end()
    tournoi.mon_arbre.preOrder(tournoi.root)
    
    print()
    print()
    print("------ PODIUM ------")
    tournoi.reset_scores(tournoi.root)
    tournoi.play_5_last_game()
    #tournoi.mon_arbre.inOrder(tournoi.root)
    ar = []
    tournoi.mon_arbre.inOrderArray(tournoi.root,ar)
    ar.sort(key= lambda x: x.score_moyen, reverse = True)
    print(ar)
    
        

if __name__ == "__main__":
    main()