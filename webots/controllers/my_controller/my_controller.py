from controller import Robot, Motor, DistanceSensor, GPS

class Init_Robot(Motor):

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        

class Motors():
    def __init__(self, speed=None):
        self.__front_right_wheel_m = Init_Robot("front right wheel motor")
        self.__front_left_wheel_m = Init_Robot("front left wheel motor")
        self.__rear_right_wheel_m = Init_Robot("rear right wheel motor")
        self.__rear_left_wheel_m = Init_Robot("rear left wheel motor")
    
    def go_forward(self, speed=5):
        self.__front_right_wheel_m.setVelocity(speed)
        self.__front_left_wheel_m.setVelocity(speed)
        self.__rear_left_wheel_m.setVelocity(speed)
        self.__rear_right_wheel_m.setVelocity(speed)

    def go_backwards(self, speed=5):

        self.__front_right_wheel_m.setVelocity(-1*speed)
        self.__front_left_wheel_m.setVelocity(-1*speed)
        self.__rear_left_wheel_m.setVelocity(-1*speed)
        self.__rear_right_wheel_m.setVelocity(-1*speed)
        print("Go Back method")

    def go_left(self, speed=5):
        self.__front_right_wheel_m.setVelocity(speed)
        self.__front_left_wheel_m.setVelocity(0)
        self.__rear_left_wheel_m.setVelocity(0)
        self.__rear_right_wheel_m.setVelocity(speed)
        print("Go Left method")

    def go_right(self, speed=5):
            self.__front_right_wheel_m.setVelocity(0)
            self.__front_left_wheel_m.setVelocity(speed)
            self.__rear_left_wheel_m.setVelocity(speed)
            self.__rear_right_wheel_m.setVelocity(0)

class Main(Robot):

    def __init__(self, speed=None):
        super().__init__()
        self.__motors = Motors()
        self.__sensors = Sensors()

    def run(self, dir='forward', speed=10):
        if dir=='backwards':
            self.__motors.go_backwards()
        elif dir=='forward':
            self.__motors.go_forward()
        elif dir=='right':
            self.__motors.go_right()
        elif dir=='left':
            self.__motors.go_left()

        self.__sensors.get_sensor()
        self.__sensors.print_sensor_value()
                


class Init_Sensors(DistanceSensor):
    def __init__(self):
        super().__init__()
        self.enable()
        #self.getValue()

class Sensors(Init_Sensors):
    
    def __init__(self):
        self.__front_right_sensor = DistanceSensor("front right distance sensor")
        self.__front_left_sensor = DistanceSensor("front left distance sensor")
        self.__rear_right_sensor = DistanceSensor("rear right distance sensor")
        self.__rear_left_sensor = DistanceSensor("rear left distance sensor")

    def get_sensor(self):
        return [self.__front_right_sensor.getValue(),
        self.__front_left_sensor.getValue(),
        self.__rear_right_sensor.getValue(),
        self.__rear_left_sensor.getValue()]

    def print_sensor_value(self):
        print("sensor value :")
        print(self.__front_left_sensor.getValue())
    
class GPS(GPS):
    def __init__(self):
        super().__init__('GPS')


TA = Main()

timestep = int(TA.getBasicTimeStep())

while TA.step(timestep) != -1:
    TA.run('right')
    pass
