# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:30 2020

@author: Leqsi
"""

from graphe import creer_graphe,creer_aretes,calcul_mat_adj

"""
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
                dico = aretes[0]
                if sommet not in dico:
                    result[sommet].append(sommet2)
    return result"""


def get_set_impostors(graph,player_dead):
    adj = calcul_mat_adj(graph)
    aretes_suspect = creer_aretes(graph,player_dead)
    result = dict()
    sommets_suspects = []
    for ar in aretes_suspect:
        for v in ar:
            sommets_suspects.append(v)
            result[v] = []
            
    for el in adj:
        for el2 in adj[el]:
            if (adj[el][el2] == 0 and el != player_dead and el in result and el2 != el):
                result[el].append(el2)
    return result

def main_step2(player_dead):
    g = creer_graphe("step2.dat")
    if player_dead not in g:
        print("Le joueur n'existe pas, voici la liste des joueurs :")
        print(g.keys())
        return
    result = get_set_impostors(g,player_dead)
    print("Ensemble des couples d'imposteurs probable :")
    print()
    for el in result:
        liste = result[el]
        for el2 in liste:
            print("{} avec {}".format(el,el2))
        print()

    
if __name__ == "__main__":
    player_dead = "Player0"
    main_step2(player_dead)
    
    
    