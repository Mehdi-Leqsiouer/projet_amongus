# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:24:50 2020

@author: Leqsi
"""

from graphe import creer_graphe


def hamilton(graph, start_v):
  size = len(graph)
  # if None we are -unvisiting- comming back and pop v
  to_visit = [None, start_v]
  path = []
  while(to_visit):
    v = to_visit.pop()
    if v :
      #print(path)
      path.append(v)
      if len(path) == size:
        break
      for x in set(graph[v])-set(path):
        to_visit.append(None) # out
        to_visit.append(x) # in
    else: # if None we are comming back and pop v
      path.pop()
  return path


def step4_algorithm(g):
    sommets = [cle for cle in g.keys()]
    #path = hamilton2(g,"Lower_Engine")
    for som in sommets:
        path = hamilton(g,som)
        if len(path) > 0:
            print("Sommet de départ : {} ".format(som))
            print(path)
        else:
            print("Pas de chemin depuis le sommet : {}".format(som))
        print()




def main():
    g = creer_graphe("step4.dat")
    print("---------- STEP 4 : Path through each room once ----------")
    step4_algorithm(g)

if __name__ == "__main__":
    main()



