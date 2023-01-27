from controller import Robot, Motor, PositionSensor

class MyRobot(Robot):
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
        self.forward()

R = MyRobot()
timestep = int(R.getBasicTimeStep())

while R.step(timestep) != -1:
    R.run()