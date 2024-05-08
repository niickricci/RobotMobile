import time
import gpiozero

class RobotMobile:
    def __init__(self):
        self.pwm = gpiozero.PWMOutputDevice(13)
        self.pwm2 = gpiozero.PWMOutputDevice(18)

        self.motor = gpiozero.DigitalOutputDevice(6)
        self.motor2 = gpiozero.DigitalOutputDevice(5)
        self.motor3 = gpiozero.DigitalOutputDevice(15)
        self.motor4 = gpiozero.DigitalOutputDevice(14)

        #Set the speed of the motors
        self.pwm.value = 0.2 
        self.pwm2.value = 0.2 
    
    #Go forward
    def forward(self):
        self.motor.on()
        self.motor2.off()
        self.motor3.on()
        self.motor4.off()
    
    #Turn right
    def rotateRight(self):
        self.motor.on()
        self.motor2.off()
        self.motor3.off()
        self.motor4.on()
    
    #Turn left
    def rotateLeft(self):
        self.motor.off()
        self.motor2.on()
        self.motor3.on()
        self.motor4.off()
    
    #Go backward
    def backward(self):
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

class InfraredSensor:
    def __init__(self):
        self.left_sensor = gpiozero.DigitalInputDevice(23)
        self.right_sensor = gpiozero.DigitalInputDevice(24)
    
    def IsOnPath(self):
        if(self.left_sensor.value == 0 and self.right_sensor.value == 0):
            return True
        else:
            return False
        
class SonarSensor:
    def __init__(self):
        self.left_sonar_trigger = gpiozero.DigitalInputDevice(8)
        self.left_sonar_echo = gpiozero.DigitalInputDevice(21)

        self.right_sonar_trigger = gpiozero.DigitalInputDevice(21)
        self.right_sonar_echo = gpiozero.DigitalInputDevice(20)
    
    def IsOnPath(self):
        if(self.left_sensor.value == 0 and self.right_sensor.value == 0):
            return True
        else:
            return False

robot = RobotMobile()
sensor = InfraredSensor()

while True:
    if(sensor.IsOnPath()):
        robot.forward()
    else:
        robot.stop()
        time.sleep(10)