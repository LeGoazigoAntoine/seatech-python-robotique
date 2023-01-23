#####  Antoine Le Goazigo   #####

import time

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

class smashBotMotor(Motor):

    def __init__(self, name="ta"):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class smashBotMotors():

    def __init__(self, speed=None):
       self.__front_right_wheel_motor = smashBotMotor('front right wheel motor')
       self.__rear_right_wheel_motor = smashBotMotor('rear right wheel motor')
       self.__front_left_wheel_motor = smashBotMotor('front left wheel motor')
       self.__rear_left_wheel_motor = smashBotMotor('rear left wheel motor')
    
    def goforward(self):
        self.__front_right_wheel_motor.setVelocity(10)
        self.__rear_right_wheel_motor.setVelocity(10)
        self.__front_left_wheel_motor.setVelocity(10)
        self.__rear_left_wheel_motor.setVelocity(10)
    
    def goback(self):
        self.__front_right_wheel_motor.setVelocity(-10)
        self.__rear_right_wheel_motor.setVelocity(-10)
        self.__front_left_wheel_motor.setVelocity(-10)
        self.__rear_left_wheel_motor.setVelocity(-10)

    def turnright(self):
        self.__front_right_wheel_motor.setVelocity(-10)
        self.__rear_right_wheel_motor.setVelocity(-10)
        self.__front_left_wheel_motor.setVelocity(10)
        self.__rear_left_wheel_motor.setVelocity(10)

    def turnleft(self):
        self.__front_right_wheel_motor.setVelocity(10)
        self.__rear_right_wheel_motor.setVelocity(10)
        self.__front_left_wheel_motor.setVelocity(-10)
        self.__rear_left_wheel_motor.setVelocity(-10)


class smashBot(Robot):
    def __init__(self, speed=None):
        super().__init__()
        self.motors=smashBotMotors()

    def goforward(self):        
            self.motors.goforward()
    
    def goback(self):        
            self.motors.goback()



robot = smashBot()
