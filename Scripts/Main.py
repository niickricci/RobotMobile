import math
import sys
import time
import gpiozero

from Dijkstra import Dijkstra
from Map import Map
from Infrared import InfraredSensor
from Motor import Motor
from Navigation import Navigation

#Test du robot
motor = Motor()
infrared = InfraredSensor()
carte = Map.carte

#Test de l'algorithme
# depart = 1
# destination = 15
# distance, chemin = Dijkstra.Chemin(carte, depart, destination)

# if chemin:
#     print("Le chemin le plus court de {} à {} est :".format(depart, destination))
#     print(chemin)
#     print("La distance totale est de", distance)
# else:
#     print("Il n'y a pas de chemin possible de {} à {}.".format(depart, destination))

#main

Navigation.parcourir_carte(1, 15) #Départ et destination