import gpiozero
import time

class Motor:
    def __init__(self):
        self.pwm = gpiozero.PWMOutputDevice(13)
        self.pwm2 = gpiozero.PWMOutputDevice(18)

        self.motor = gpiozero.DigitalOutputDevice(6)
        self.motor2 = gpiozero.DigitalOutputDevice(5)
        self.motor3 = gpiozero.DigitalOutputDevice(15)
        self.motor4 = gpiozero.DigitalOutputDevice(14)

        #Set the speed of the motors
        self.pwm.value = 0.33 
        self.pwm2.value = 0.33 
    
    #Go forward
    def forward(self):
        self.pwm.value = 0.32
        self.pwm2.value = 0.32
        self.motor.on()
        self.motor2.off()
        self.motor3.on()
        self.motor4.off()
    
    #Turn right
    def rotateRight(self):
        self.pwm.value = 0.5
        self.pwm2.value = 0.6
        self.motor.on()
        self.motor2.off()
        self.motor3.off()
        self.motor4.on()
    
    #Turn left
    def rotateLeft(self):
        self.pwm.value = 0.5
        self.pwm2.value = 0.6
        self.motor.off()
        self.motor2.on()
        self.motor3.on()
        self.motor4.off()
    
    #Go backward
    def backward(self):
        self.pwm.value = 0.4
        self.pwm2.value = 0.4
        self.motor.off()
        self.motor2.on()
        self.motor3.off()
        self.motor4.on()

    #Stop
    def stop(self):
        self.motor.off()
        self.motor2.off()
        self.motor3.off()
        self.motor4.off()
        
    def rotateNode(self, current_node):
        #Point 7
        if(current_node == 2):
            self.forward()
            time.sleep(0.1)
        #Point 6
        if(current_node == 3):
            self.rotateRight()
            time.sleep(2)
        #Point 8
        if(current_node == 4): 
            self.rotateLeft()
            time.sleep(1.5)
        #Point 9
        if(current_node == 5): 
            self.rotateLeft()
            time.sleep(1.5)
        #Point 15
        if(current_node == 6): 
            self.forward()
            time.sleep(0.1)
        #Point 14
        if(current_node == 7):
            # self.rotateRight()
            self.rotateLeft()
            time.sleep(1.5)
        #Point 17
        if(current_node == 8): 
            self.forward()
            time.sleep(0.1)
        
        