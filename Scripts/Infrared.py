# import gpiozero
# import threading
# from Motor import Motor
# import time

# class InfraredSensor:
    # def __init__(self):
        # self.left_sensor = gpiozero.DigitalInputDevice(23)
        # self.right_sensor = gpiozero.DigitalInputDevice(24)
    
    # def IsOnPath(self):
            # time.sleep(0.1)
            # if(self.left_sensor.value == 1 and self.right_sensor.value == 1):
                # return False
            # else:
                # return True
        
    # def IsOnLeft(self):
            # time.sleep(0.1)

            # if(self.left_sensor.value == 1 and self.right_sensor.value == 0):
                # return True
            # else:
                # return False
    
    # def IsOnRight(self):
            # time.sleep(0.1)

            # if(self.right_sensor.value == 1 and self.left_sensor.value == 0):
                # return True
            # else:
                # return False
import gpiozero
import time
import threading

class InfraredSensor:
    def __init__(self):
        self.left_sensor = gpiozero.DigitalInputDevice(23)
        self.right_sensor = gpiozero.DigitalInputDevice(24)
        self.lock = threading.Lock()
    
    def IsOnPath(self):
        count = 0
        with self.lock:
            for i in range(3):  
                if self.left_sensor.value == 1 and self.right_sensor.value == 1:
                    count += 1
                time.sleep(0.02)  
        return count < 1 
    
    def IsOnLeft(self):
        count = 0
        with self.lock:
            for i in range(3):  
                if self.left_sensor.value == 1 and self.right_sensor.value == 0:
                    count += 1
            time.sleep(0.001)  
        return count >= 3  
    def IsOnRight(self):
        count = 0
        with self.lock:
            for i in range(3):  
                if self.right_sensor.value == 1 and self.left_sensor.value == 0:
                    count += 1
            time.sleep(0.001)  
        return count >= 3  
