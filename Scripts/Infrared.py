import gpiozero

class InfraredSensor:
    def __init__(self):
        self.left_sensor = gpiozero.DigitalInputDevice(23)
        self.right_sensor = gpiozero.DigitalInputDevice(24)
    
    def IsOnPath(self):
        if(self.left_sensor.value == 0 and self.right_sensor.value == 0):
            return True
        else:
            return False
        
    def IsOnLeft(self):
        if(self.left_sensor.value == 1):
            return True
        else:
            return False
    
    def IsOnRight(self):
        if(self.right_sensor.value == 1):
            return True
        else:
            return False