# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:30 2020

@author: Leqsi
"""

from graphe import creer_graphe,creer_aretes

def get_set_impostors(graph,player_dead):
    aretes_suspect = creer_aretes(graph,player_dead)
    Noeuds = [cle for cle in graph.keys()]
    sommets_suspects = []
    result = dict()
    #print(aretes_suspect)
    for ar in aretes_suspect:
        for v in ar:
            sommets_suspects.append(v)
            result[v] = []
    #print(sommets_suspects)
    
    for sommet in sommets_suspects:
        #print("suspect : {}".format(sommet))
        for sommet2 in Noeuds:
            if sommet2 != sommet:
                aretes = creer_aretes(graph,sommet2)
                #print(sommet2)
                #print(aretes)
                dico = aretes[0]
                if sommet not in dico:
                    result[sommet].append(sommet2)
                    #print("new suspect : {}".format(sommet2))
        print()
    return result


def main():
    g = creer_graphe("step2.dat")
    result = get_set_impostors(g,"Player0")
    print("Ensemble des couples d'imposteurs probable :")
    print()
    for el in result:
        liste = result[el]
        for el2 in liste:
            print("{} avec {}".format(el,el2))
        print()
    
if __name__ == "__main__":
    main()
    
    
    