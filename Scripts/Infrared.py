import gpiozero
import threading
from Motor import Motor
import time

class InfraredSensor:
    def __init__(self):
        self.left_sensor = gpiozero.DigitalInputDevice(23)
        self.right_sensor = gpiozero.DigitalInputDevice(24)
        self.lock = threading.Lock()
    
    def IsOnPath(self):
        with self.lock:
            time.sleep(0.1)
            if(self.left_sensor.value == 0 and self.right_sensor.value == 0):
                print("On path")
                return True
            elif(self.left_sensor.value == 1 and self.right_sensor.value == 1):
                return False
            else:
                return True
        
    def IsOnLeft(self):
        with self.lock:
            time.sleep(0.1)

            if(self.left_sensor.value == 1 and self.right_sensor.value == 0):
                return True
            else:
                return False
    
    def IsOnRight(self):
        with self.lock:
            time.sleep(0.1)

            if(self.right_sensor.value == 1 and self.left_sensor.value == 0):
                return True
            else:
                return False