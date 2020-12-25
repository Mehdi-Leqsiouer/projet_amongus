# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:30 2020

@author: Leqsi
"""

from graphe import creer_graphe,creer_aretes,calcul_mat_adj

def get_set_impostors(graph,player_dead):
    """This function create the adjacency matrix and return the set of
    probable impostor based on the matrix"""
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
    """Main function"""
    g = creer_graphe("step2.dat")
    if player_dead not in g:
        print("The player doesn't exist, here is the list of players : :")
        print(g.keys())
        return
    result = get_set_impostors(g,player_dead)
    print("Set of probable impostors :")
    print()
    for el in result:
        liste = result[el]
        for el2 in liste:
            print("{} with {}".format(el,el2))
        print()

    
if __name__ == "__main__":
    player_dead = "Player0"
    main_step2(player_dead)
    
    
    