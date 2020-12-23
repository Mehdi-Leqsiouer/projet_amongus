# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:35:31 2020

@author: Leqsi
"""

import random

class Player(object):
    def __init__(self,p_id,score,nb_games):
        #self.score = 0
        self.id = p_id
        self.score_moyen = score
        self.impostor = False
        self.nb_games = nb_games
        
    def reset_score(self):
        self.score_moyen = 0
        
    def __repr__(self):
        return "Id : "+str(self.id)+" mean score : "+str(self.score_moyen) + " nb games : "+str(self.nb_games)#+" imposteur ? : "+str(self.impostor)
        
    def setMeanScore(self,p_score):
        self.score_moyen = p_score
    
    def incrementNbGames(self):
        self.nb_games += 1


class TreeNode(Player): 
	def __init__(self,score,p_id,nb_games):
		Player.__init__(self,p_id,score,nb_games)
		self.left = None
		self.right = None
		self.height = 1
        
	def __repr__(self):
		return Player.__repr__(self)

class AVL_Tree(object): 
    
    def insert(self, root, key,p_id,nb_games): 
        if not root: 
            return TreeNode(key,p_id,nb_games) 
        elif key < root.score_moyen: 
            root.left = self.insert(root.left, key,p_id,nb_games) 
        else: 
            root.right = self.insert(root.right, key,p_id,nb_games) 

        root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

        balance = self.getBalance(root) 
        if balance > 1 and key < root.left.score_moyen: 
            return self.rightRotate(root) 

        if balance < -1 and key >= root.right.score_moyen: 
            return self.leftRotate(root) 

        if balance > 1 and key >= root.left.score_moyen: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        
        if balance < -1 and key < root.right.score_moyen: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 

    def delete(self, root, key,p_id,nb_games ): 

        if not root: 
            return root 

        elif key < root.score_moyen: 
            root.left = self.delete(root.left, key,p_id,nb_games) 

        elif key > root.score_moyen: 
            root.right = self.delete(root.right, key,p_id,nb_games) 

        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 

            elif root.right is None:
                temp = root.left 
                root = None
                return temp 

            temp = self.getMinValueNode(root.right) 
            root.score_moyen = temp.score_moyen 
            root.id = temp.id
            root.nb_games = temp.nb_games
            root.right = self.delete(root.right, 
									temp.score_moyen,temp.id,temp.nb_games) 

        if root is None: 
            return root 

        root.height = 1 + max(self.getHeight(root.left), 
							self.getHeight(root.right)) 

        balance = self.getBalance(root) 

        if balance > 1 and self.getBalance(root.left) > 0: 
            return self.rightRotate(root) 

        if balance < -1 and self.getBalance(root.right) < 0: 
            return self.leftRotate(root) 

        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 

    def leftRotate(self, z): 

        y = z.right 
        T2 = y.left 

        y.left = z 
        z.right = T2 

        z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

        return y 

    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 
 
        z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

        return y 
    
    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 

    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 

        return self.getMinValueNode(root.left)
                              
    def getMaxValueNode(self, root): 
        if root is None or root.right is None: 
            return root 

        return self.getMaxValueNode(root.right)  

    def changeKey(self,root, oldVal, newVal,id_p,nb_games): 
      
        # First delete old key value  
        root = self.delete(root, oldVal,id_p,nb_games)  
      
        # Then insert new key value  
        root = self.insert(root, newVal,id_p,nb_games) 
      
        # Return new root  
        return root                            
    
    def preOrder(self, root): 
        if not root: 
            return

        print("Score : {} id : {} nb games {} ".format(root.score_moyen,root.id,root.nb_games), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right)  
        
        
    def inOrder(self, root): 
        if not root: 
            return
      
        self.preOrder(root.left) 
        print("Score : {} id : {} ".format(root.score_moyen,root.id), end="") 
        self.preOrder(root.right) 
        
    def inOrder_desc(self, root): 
        if not root: 
            return
      
        self.preOrder(root.right) 
        print("Score : {} id : {} ".format(root.score_moyen,root.id), end="") 
        self.preOrder(root.left) 
        
    def postOrder(self, root): 
        if not root: 
            return
    
        self.preOrder(root.left) 
        self.preOrder(root.right)  
        print("Score : {} id : {} ".format(root.score_moyen,root.id), end="") 
        
    def searchmin(self,root):
        if root.left == None:
            return root
        return self.searchmin(root.left)
    
    def deletemin(self,root):
        if root == None:
            return root
        return self.delete(root,self.searchmin(root).score_moyen)

    def inOrderArray(self, root, tab): 
        if root: 
            self.inOrderArray(root.left,tab)
            tab.append(root)
            self.inOrderArray(root.right,tab)
        return tab 
      
    # Returns Random node  
    def randomNode(self,root,size):  
        r = random.randint(0,size)
        if r == 0 or root == None:
            return root
        elif root.left != None and 1 <= r and r <= self.getHeight(root.left):
            return self.randomNode(root.left,size)
        else:
            return self.randomNode(root.right,size)
        
    def isAVL(self, root): 
        return (True if abs(self.getBalance(root))<=1 else False)   
    
    def size(self,root): 
        if root is None: 
            return 0 
        else: 
            return (self.size(root.left)+ 1 + self.size(root.right)) 
    
    


"""myTree = AVL_Tree() 
root = None
nums = [10,20,15,25,30,16,18,19] 

for num in nums: 
	root = myTree.insert(root, num) 


myTree.preOrder(root) 
print() 

#delete 
key = 10
root = myTree.delete(root, key) 

myTree.preOrder(root) 
print() """


