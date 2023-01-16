######### Importation du temps #############
import time

######### Classe du robot ##############

class Robot():
    name = ""
    power = False
    #__current_speed = 0
    battery_level = 0
    current_state = ''
    current_speed = 0
    states = ['shutown', 'running']
    
    def __init__(self, name=None):
        self.name = name
        self.power = True
        self.current_state = self.states[1]

    def off(self):
        self.power = False
        self.current_state = self.states[0]

    def charging(self):
        i = 0
        while i < 100:
            self.battery_level += 1
            time.sleep(0.1)
            i += 1
            print(self.battery_level)

    def move(self,speed):	
        if type(speed) == int:
            self.current_speed = speed

    def stop(self):
        self.current_speed = 0
	
    def speed(self):
      return self.current_speed

    def resume(self):
        print("\nVoici un resume du robot : \n")
        print("Le Robot s'appelle %s"%(r.name))
        print("Le Robot est %s"%(r.current_state))
        print("Le niveau de la batterie est de " + f'{r.battery_level}'+ " %.")
        print("Vitesse du robot est de " + f'{r.speed()}' + " cm/s")
        print("\n")


######### MAIN #############

#r = Robot(name='Marie')

#print("Le Robot s'appelle %s"%(r.name))
#print("Le Robot est %s"%(r.current_state))
#print("Le niveau de la batterie est de " + f'{r.battery_level}'+ " %.")
#r.charging()
#print("Le niveau de la batterie est de " + f'{r.battery_level}'+ " %.")
#r.move(50)
#print("Vitesse du robot est de " + f'{r.speed()}' + " cm/s")
#r.stop()
#print("Vitesse du robot est de " + f'{r.speed()}' + " cm/s")
#r.resume()
#r.off()
#print("Le Robot est %s"%(r.current_state))