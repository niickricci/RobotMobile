import sys

class Dijkstra:

    def Chemin(carte, depart, destination):

        Inf = sys.maxsize #Infini
        nodes_list = [(0, depart, [])] #Liste de noeuds
        visited = set() #Noeuds visite
    
        while nodes_list: 
            nodes_list.sort()  # Trie la liste des noeuds par ordre croissant
            (total_distance, node, trajet) = nodes_list.pop(0)  #Prend le premier noeud de la liste
            if node not in visited: #Si le noeud n'a pas ete visite
                trajet = trajet + [node]  #Ajoute le noeud au chemin
                if node == destination: #Si le noeud est la destination
                    return total_distance, trajet #Return distance + chemin
                visited.add(node) #Ajoute le noeud a la destination
                for linked_node, distance in carte[node].items(): #Pour chaque noeud connecte au noeud actuel
                    nodes_list.append((total_distance + distance, linked_node, trajet)) #Ajoute le le noeud connecte a la liste des noeuds
    
        return Inf, None