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
        
    
    def delete_last10(self):
        for i in range (10):
            self.root = self.mon_arbre.deletemin(self.root)

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
        

if __name__ == "__main__":
    main()