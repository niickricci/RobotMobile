import math
import sys
import time
import gpiozero
import threading

from Dijkstra import Dijkstra
from Map import Map
from Infrared import InfraredSensor
from Motor import Motor
from Navigation import Navigation

#Test du robot
motor = Motor()
infrared = InfraredSensor()
carte = Map.carte
lock = threading.Lock()

#Test de l'algorithme
depart = 1
current_node = depart
destination = 9
# distance, chemin = Dijkstra.Chemin(carte, depart, destination)

# if chemin:
#     print("Le chemin le plus court de {} à {} est :".format(depart, destination))
#     print(chemin)
#     print("La distance totale est de", distance)
# else:
#     print("Il n'y a pas de chemin possible de {} à {}.".format(depart, destination))

#main
        
# Navigation.parcourir_carte(1, 15) #Départ et destination
while current_node != destination:
    while not infrared.IsOnPath():
        motor.stop()
        time.sleep(1)
        current_node += 1
        print("Current node:", current_node)
        motor.rotateNode(current_node)
        time.sleep(0.35)
    
    while infrared.IsOnLeft() or infrared.IsOnRight():
        if infrared.IsOnLeft():
            motor.rotateLeft()
        elif infrared.IsOnRight():
            motor.rotateRight()
        time.sleep(0.15)
        motor.stop()
    
    motor.forward()

print("Arrivé à destination | Current node:", destination)
motor.stop()