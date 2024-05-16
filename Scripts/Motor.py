import gpiozero

class Motor:
    def __init__(self):
        self.pwm = gpiozero.PWMOutputDevice(13)
        self.pwm2 = gpiozero.PWMOutputDevice(18)

        self.motor = gpiozero.DigitalOutputDevice(6)
        self.motor2 = gpiozero.DigitalOutputDevice(5)
        self.motor3 = gpiozero.DigitalOutputDevice(15)
        self.motor4 = gpiozero.DigitalOutputDevice(14)

        #Set the speed of the motors
        self.pwm.value = 0 
        self.pwm2.value = 0 
    
    #Go forward
    def forward(self):
        self.pwm.value = 0.4
        self.pwm2.value = 0.4
        self.motor.on()
        self.motor2.off()
        self.motor3.on()
        self.motor4.off()
    
    #Turn right
    def rotateRight(self):
        self.pwm.value = 0.6
        self.pwm2.value = 0.7
        self.motor.on()
        self.motor2.off()
        self.motor3.off()
        self.motor4.on()
    
    #Turn left
    def rotateLeft(self):
        self.pwm.value = 0.6
        self.pwm2.value = 0.7
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