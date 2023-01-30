from controller import Robot, Motor, PositionSensor
import time
class Mouvement(Robot):
    def __init__(self):
        Robot.__init__(self)

        self.__back_left_motor = self.getDevice('back_left_wheel_joint')
        self.__back_right_motor = self.getDevice('back_right_wheel_joint')
        self.__front_left_motor = self.getDevice('front_left_wheel_joint')
        self.__front_right_motor = self.getDevice('front_right_wheel_joint')

        self.__back_left_sensor = self.getDevice('back_left_wheel_joint_sensor')
        self.__back_right_sensor = self.getDevice('back_right_wheel_joint_sensor')
        self.__front_left_sensor = self.getDevice('front_left_wheel_joint_sensor')
        self.__front_right_sensor = self.getDevice('front_right_wheel_joint_sensor')

        self.__back_left_motor.setPosition(float('inf'))
        self.__back_right_motor.setPosition(float('inf'))
        self.__front_left_motor.setPosition(float('inf'))
        self.__front_right_motor.setPosition(float('inf'))

        self.__back_left_motor.setVelocity(0)
        self.__back_right_motor.setVelocity(0)
        self.__front_left_motor.setVelocity(0)
        self.__front_right_motor.setVelocity(0)

        __target = [0.0, 0.0, 0.0]
        __speed = [0.0, 0.0, 0.0, 0.0]

    def stop(self):
        self.__back_left_motor.setVelocity(0)
        self.__back_right_motor.setVelocity(0)
        self.__front_left_motor.setVelocity(0)
        self.__front_right_motor.setVelocity(0)

    def forward(self):
        self.__back_left_motor.setVelocity(10)
        self.__back_right_motor.setVelocity(10)
        self.__front_left_motor.setVelocity(10)
        self.__front_right_motor.setVelocity(10)

    def backward(self):
        self.__back_left_motor.setVelocity(10)
        self.__back_right_motor.setVelocity(10)
        self.__front_left_motor.setVelocity(10)
        self.__front_right_motor.setVelocity(10)

    def turn_left(self):
        self.__back_left_motor.setVelocity(-10)
        self.__back_right_motor.setVelocity(10)
        self.__front_left_motor.setVelocity(-10)
        self.__front_right_motor.setVelocity(10)

    def turnright(self):
        self.__back_left_motor.setVelocity(10)
        self.__back_right_motor.setVelocity(-10)
        self.__front_left_motor.setVelocity(10)
        self.__front_right_motor.setVelocity(-10)

    def run(self):
        for i in [0, 1, 2, 3]:
            time.sleep(2)
            if i==1:
                self.turnright()
                self.forward()

            if i==2:
                self.turn_left()
                self.backward()

            if i==3:
                self.turnright()
                self.backward()
                i = 0

TA = Mouvement()
timestep = int(TA.getBasicTimeStep())

while TA.step(timestep) != -1:
    TA.run()