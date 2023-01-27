class RobotControl:
    def init(self):
        Robot.__init__(self)

        self.__back_left_motor = self.getDevice('back_left_wheel_joint')
        self.__back_right_motor = self.getDevice('back_right_wheel_joint')
        self.__front_left_motor = self.getDevice('front_left_wheel_joint')
        self.__front_right_motor = self.getDevice('front_right_wheel_joint')

        self.__back_left_sensor = self.getDevice('back_left_wheel_joint_sensor')
        self.__back_right_sensor = self.getDevice('back_right_wheel_joint_sensor')
        self.__front_left_sensor = self.getDevice('front_left_wheel_joint_sensor')
        self.__front_right_sensor = self.getDevice('front_right_wheel_joint_sensor')
        # ds.enable(timestep)

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
        self.back_left_motor.setVelocity(0)
        self.back_right_motor.setVelocity(0)
        self.front_left_motor.setVelocity(0)
        self.front_right_motor.setVelocity(0)

    def forward(self):
        self.back_left_motor.setVelocity(100.0)
        self.back_right_motor.setVelocity(100.0)
        self.front_left_motor.setVelocity(100.0)
        self.front_right_motor.setVelocity(100.0)

    def backward(self):
        self.back_left_motor.setVelocity(-100.0)
        self.back_right_motor.setVelocity(-100.0)
        self.front_left_motor.setVelocity(-100.0)
        self.front_right_motor.setVelocity(-100.0)

    def left_stationary(self):
        self.back_left_motor.setVelocity(-10.0)
        self.back_right_motor.setVelocity(10.0)
        self.front_left_motor.setVelocity(-10.0)
        self.front_right_motor.setVelocity(10.0)

    def right_stationary(self):
        self.back_left_motor.setVelocity(10.0)
        self.back_right_motor.setVelocity(-10.0)
        self.front_left_motor.setVelocity(10.0)
        self.front_right_motor.setVelocity(-10.0)

    def run(self):
        self.forward()

Robot = RobotControl()
timestep = int(Robot.getBasicTimeStep())

while Robot.step(timestep) != -1:
    Robot.run()
