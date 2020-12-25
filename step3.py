# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:27:14 2020

@author: Leqsi
"""

import math
from graphe import creer_graphe,creer_aretes,calcul_mat_poids

def calcul_dijsktra (graphe, sommet_start, sommet_fin=None): 
    """Implementation of Dijsktra pathfinding algorithm """
    
    
    """All vertices"""
    sommets_S = [cle for cle in graphe.keys()]
    
    """Starting vertex check"""
    if sommet_start not in sommets_S:
        print ('Erreur: le noeud de départ {} n\'existe pas'.format(sommet_start))
        return
    
    if sommet_start == sommet_fin:
        return "Start = goal"
    
     
    """Vertices not computed 
    """
    sommets_E = sommets_S.copy()
    sommets_E.remove(sommet_start)
    
    """Weight matrix"""
    poids = calcul_mat_poids(graphe)

    #print(poids)
    distances_E = {}
    distances_E[sommet_start] = 0

    for sommet in sommets_E:
        if (sommet != sommet_start and poids[sommet_start][sommet] != math.inf):
            distances_E[sommet] = poids[sommet_start][sommet]
        else:
            distances_E[sommet] = math.inf
    
    pred = {}
    aretes_depart = creer_aretes(graphe,sommet_start)
    for v in aretes_depart:
        for v2 in v:
            pred[v2] = sommet_start
    #print(pred)
    sommet_u = min(sommets_E, key=(lambda k: distances_E[k]))
    #print(sommet_u)
    aretes_u = creer_aretes(graphe, sommet_u)  
    #print(aretes_u)
    while sommets_E:  
        sommet_u = min(sommets_E, key=(lambda k: distances_E[k]))
        #print(sommet_u)
        aretes_u = creer_aretes(graphe, sommet_u) 
        #print(aretes_u)
        for ar in aretes_u:        
            voisin_existe = False
            sommet_v = None
            for v in ar:
                if (v in sommets_E):
                    voisin_existe = True
                    sommet_v = v
                    if voisin_existe:   
                        #update distance
                        if(distances_E[sommet_u] != math.inf):
                            dist = distances_E[sommet_u] + poids[sommet_u][sommet_v]
                        else:
                            dist = poids[sommet_u][sommet_v]
                        if (dist < distances_E[sommet_v] or distances_E[sommet_v] == math.inf):
                            distances_E[sommet_v] = dist
                            #print(pred)
                        if(sommet_v not in pred):
                            pred[sommet_v] = sommet_u
                #print(distances_E)
        #print(distances_E)      
        #update vertices computed list
        sommets_E.remove(sommet_u)
    #finding the path
    #print(distances_E)
    if sommet_fin:
        chemin = []
        sommet_u = sommet_fin
        chemin.append(sommet_fin)
        while(sommet_u != sommet_start):
            for el in pred:
                if(el  == sommet_u):
                    chemin.append(pred[el])
                    sommet_u = pred[el]      
        return distances_E, chemin
    
    return distances_E


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    """Implementation of BFS pathfinding """
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]    
    
    """All vertices"""
    sommets_S = [cle for cle in graph.keys()]
    
    """Starting vertex"""
    if start not in sommets_S:
        print ('Erreur: le noeud de départ {} n\'existe pas'.format(start))
        return
    
     
    """Vertices not computed
    """
    sommets_E = sommets_S.copy()
    sommets_E.remove(start)
    
    """Weight matrix"""
    poids = calcul_mat_poids(graph)

    #print(poids)
    distances_E = {}
    distances_E[start] = 0

    for sommet in sommets_E:
        if (sommet != start and poids[start][sommet] != math.inf):
            distances_E[sommet] = poids[start][sommet]
        else:
            distances_E[sommet] = math.inf
 
    # return path if start is goal
    if start == goal:
        return "Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                if(distances_E[node] != math.inf):
                    dist = distances_E[node] + poids[node][neighbour]
                else:
                    dist = poids[node][neighbour]
                if (dist < distances_E[neighbour] or distances_E[neighbour] == math.inf):
                    distances_E[neighbour] = dist
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path,distances_E
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


def floydWarshall(graph):
    """Implementation of Floyd Warshall algorithm that return all
    weights for each pair of vertices"""
    mat_poids = calcul_mat_poids(graph)
    for k in mat_poids:
        for i in mat_poids:
            for j in mat_poids:
                if (i == j):
                    mat_poids[i][j] = 0
                else:
                    mat_poids[i][j] = min(mat_poids[i][j] ,mat_poids[i][k]+ mat_poids[k][j])
    return mat_poids


def step3_3(depart,arriver):
    """Main function that call pathfinding function for 3) question"""
    g_crewmate = creer_graphe("step4.dat")
    
    g_impostor = creer_graphe("step3_impostor.dat")
    if depart not in g_crewmate or arriver not in g_crewmate:
        if depart not in g_crewmate:
            print("The starting vertex doesn't exist in the list of vertex.")
        if arriver not in g_crewmate:
            print("The ending vertex doesn't exist in the list of vertex.")
        print("Here is the list of vertex : ")
        print(g_crewmate.keys())
        return
    
    print("\n---------- STEP 3 : shortest path from A to B ----------")
    dij = bfs_shortest_path(g_crewmate, depart, arriver)
    distances = dij[1]
    chemin = dij[0]
    #chemin.reverse()
    print("Path & length as crewmate : ")
    print("\nPath {}".format(chemin))
    print("Weight : {}".format(distances[arriver]))
    print()    
    
    dij = calcul_dijsktra(g_impostor, depart, arriver)
    distances = dij[0]
    chemin = dij[1]
    chemin.reverse()
    print("Path & length as impostor : ")
    print("\nPath {}".format(chemin))
    print("Weight : {}".format(distances[arriver]))
    print()
    
def step3_4():
    """Main function that call Floyd Warshall for 4) question"""
    g_impostor = creer_graphe("step3_impostor.dat")
    print("---------- STEP 3 : All shortest path from each pair of rooms ----------")
    d = floydWarshall(g_impostor)
    for el in d:
        print ("Starting room : {} ".format(el))
        #print(d[el])
        for el2 in d[el]:
            print("Ending room : {} , Weight : {}".format(el2,d[el][el2]))
        print()
    
if __name__ == "__main__":
    depart = "Navigations"
    arriver = "Upper_Engine"
    step3_3(depart,arriver)
    step3_4()



