from Dijkstra import Dijkstra
from Motor import Motor
from Map import Map
import time



class Navigation:
    
    def parcourir_carte(self, depart, destination):
        # depart = 1  # Départ 
        current_node = depart
        last_node = depart
        # destination = 15  # Destination 
        dure = 1 #Dure pour chaque distance
        dure_90 = 1 #Dure rotation de 90°
        dure_180 = 2 #Dure rotation de 180°
        dure_360 = 3 #Dure rotation de 360°
        carte = Map.carte
        motor = Motor()

        distance, chemin = Dijkstra.Chemin(carte, depart, destination)

        while current_node != destination:
            if chemin: #Si un chemin existe
                print("Le chemin le plus court de {} à {} est :".format(current_node, destination))
                print(chemin)
                print("La distance totale est de", distance)
                print ("Noeud actuel : ", current_node)

                for node in chemin:
                    next_node = node
                    if node == current_node:
                        continue 
                    if node == destination:
                        print("Arrivé à destination.")
                        break
                    #Noeud 1 
                    if(current_node == 1 and next_node == 2):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 2 
                    if(current_node == 2 and next_node == 1 and last_node == 3):
                        motor.backward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 2 and next_node == 1 and last_node == 4):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 2 and next_node == 3 and last_node == 1):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 2 and next_node == 3 and last_node == 4):
                        motor.rotateLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 2 and next_node == 4 and last_node == 1):
                        motor.rotateLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 2 and next_node == 4 and last_node == 3):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 3
                    if(current_node == 3 and next_node == 2):
                        motor.backward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 4 
                    if(current_node == 4 and next_node == 2 and last_node == 5):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 4 and next_node == 2 and last_node == 6):
                        motor.rotateLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 4 and next_node == 5 and last_node == 2):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 4 and next_node == 5 and last_node == 6):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 4 and next_node == 6 and last_node == 2):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 4 and next_node == 6 and last_node == 5):
                        motor.rotateLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 5
                    if(current_node == 5 and next_node == 4 and last_node == 11):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 5 and next_node == 4 and last_node == 8):
                        motor.rotateLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 5 and next_node == 8 and last_node == 4):
                        motor.rotateRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 5 and next_node == 8 and last_node == 11):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 6
                    if(current_node == 6 and next_node == 4 and last_node == 7):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 6 and next_node == 4 and last_node == 8):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 6 and next_node == 7 and last_node == 4):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 6 and next_node == 7 and last_node == 8):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 6 and next_node == 8 and last_node == 4):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 6 and next_node == 8 and last_node == 7):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 7
                    if(current_node == 7 and next_node == 6):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Intersection Noeud 8
                    if(current_node == 8 and next_node == 5 and last_node == 9):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 8 and next_node == 5 and last_node == 6):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 8 and next_node == 9 and last_node == 5):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 8 and next_node == 9 and last_node == 6):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 9
                    if(current_node == 9 and next_node == 8 and last_node == 10):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 9 and next_node == 8 and last_node == 15):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 9 and next_node == 10 and last_node == 8):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 9 and next_node == 10 and last_node == 15):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 9 and next_node == 15 and last_node == 8):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 9 and next_node == 15 and last_node == 10):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 10
                    if(current_node == 10 and next_node == 9):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 11
                    if(current_node == 11 and next_node == 5 and last_node == 12):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 11 and next_node == 5 and last_node == 5):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 11 and next_node == 12 and last_node == 5):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 12
                    if(current_node == 12 and next_node == 11 and last_node == 13):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 12 and next_node == 11 and last_node == 11):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 13
                    if(current_node == 13 and next_node == 12 and last_node == 14):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 13 and next_node == 12 and last_node == 12):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 13 and next_node == 14 and last_node == 16):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 13 and next_node == 12 and last_node == 16):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 14
                    if(current_node == 14 and next_node == 13 and last_node == 15):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 13 and last_node == 13):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 15 and last_node == 13):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 15 and last_node == 17):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 13 and last_node == 17):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 17 and last_node == 13):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 14 and next_node == 17 and last_node == 15):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 15
                    if(current_node == 15 and next_node == 9 and last_node == 14):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 15 and next_node == 9 and last_node == 9):
                        motor.turnLeft()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 15 and next_node == 14 and last_node == 9):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 15 and next_node == 14 and last_node == 14):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if (current_node == 15 and next_node == 19 and last_node == 14):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure * carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if (current_node == 15 and next_node == 19 and last_node == 9):
                        motor.forward()
                        time.sleep(dure * carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if (current_node == 15 and next_node == 19 and last_node == 19):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure * carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 16
                    if(current_node == 16 and next_node == 13):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 17
                    if(current_node == 17 and next_node == 14 and last_node == 18):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 17 and next_node == 14 and last_node == 19):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 17 and next_node == 18 and last_node == 14):
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 17 and next_node == 18 and last_node == 19):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 17 and next_node == 19 and last_node == 14):
                        motor.turnRight()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 17 and next_node == 19 and last_node == 18):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 18
                    if(current_node == 18 and next_node == 17):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    #Noeud 19
                    if(current_node == 19 and next_node == 15 and last_node == 17):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 19 and next_node == 15 and last_node == 15):
                        motor.turnLeft()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 19 and next_node == 17 and last_node == 15):
                        motor.turnLeft()
                        time.sleep(dure_90)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    if(current_node == 19 and next_node == 17 and last_node == 17):
                        motor.turnRight()
                        time.sleep(dure_180)
                        motor.forward()
                        time.sleep(dure*carte[current_node][next_node])
                        motor.stop()
                        last_node = current_node
                        current_node = node
                        continue
                    else:
                        print("Il n'y a pas de chemin possible de {} à {}.".format(current_node, destination))
                        break
            else:
                print("Il n'y a pas de chemin possible de {} à {}.".format(current_node, destination))
                break