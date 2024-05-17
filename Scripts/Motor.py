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
        self.pwm.value = 0.5
        self.pwm2.value = 0.5
        self.motor.on()
        self.motor2.off()
        self.motor3.on()
        self.motor4.off()
    
    #Turn right
    def rotateRight(self):
        self.pwm.value = 0.615
        self.pwm2.value = 0.53
        self.motor.on()
        self.motor2.off()
        self.motor3.off()
        self.motor4.on()
    
    #Turn left
    def rotateLeft(self):
        self.pwm2.value = 0.5
        self.pwm2.value = 0.76
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
    #Chemin 1
    def rotatenode(self, current_node):
        #point 7
        if(current_node == 2):
            self.forward()
            time.sleep(0.1)
        #point 6
        if(current_node == 3):
            self.rotateright()
            #self.rotateleft()
            time.sleep(1.8)
        #point 8
        if(current_node == 4): 
            self.rotateleft()
            time.sleep(1.5)
        #point 9
        if(current_node == 5): 
            self.rotateleft()
            time.sleep(1.5)
        #point 15
        if(current_node == 6): 
            self.forward()
            time.sleep(0.1)
        #point 14
        if(current_node == 7):
            self.rotateright()
            #self.rotateleft()
            time.sleep(1.5)
        #point 17
        if(current_node == 8): 
            self.forward()
            time.sleep(0.1)
    ##Chemin 2        
    # def rotateNode(self, current_node):
       
        # #Point 15
        # if(current_node == 2):
            # self.rotateLeft()
            # #self.rotateLeft()
            # time.sleep(1.5)
        # #Point 14
        # if(current_node == 3): 
            # self.forward()
            # time.sleep(0.1)
        # #Point 16
        # if(current_node == 4): 
            # self.rotateRight()
            # time.sleep(1.5)
    ##Chemin 3     
    # def rotateNode(self, current_node):
       
        # #Point 15
        # if(current_node == 2):
            # self.rotateRight()
            # time.sleep(1.5)
        # #Point 14
        # if(current_node == 3): 
            # self.forward()
            # time.sleep(0.1)
        # #Point 16
        # if(current_node == 4): 
            # self.forward()
            # time.sleep(0.1)
        # if(current_node == 5): 
            # self.rotateLeft()
            # time.sleep(1.5)
        
        
        
        