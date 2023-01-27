from controller import Robot, Motor, DistanceSensor
import time

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

class Moteurs():
    
    __vitesseGauche = 5
    __vitesseDroit = 5
    __moteurGauche = robot.getDevice('left wheel motor')
    __moteurDroit = robot.getDevice('right wheel motor')

    def __init__(self):
        self.__moteurGauche.setPosition(float('inf'))
        self.__moteurDroit.setPosition(float('inf'))
        self.__moteurGauche.setVelocity(0)
        self.__moteurDroit.setVelocity(0)

    def avancer(self):
        self.__moteurGauche.setVelocity(5)
        self.__moteurDroit.setVelocity(5)
        print("J'avance")

    def reculer(self):
        self.__moteurGauche.setVelocity(-5)
        self.__moteurDroit.setVelocity(-5)
        print("Je recule")

    def turnGauche(self):
        self.__moteurGauche.setVelocity(-5)
        self.__moteurDroit.setVelocity(5)
        print('Je tourne à gauche')
    
    def turnDroite(self):
        self.__moteurGauche.setVelocity(5)
        self.__moteurDroit.setVelocity(-5)
        print('Je tourne à droite')



class Capteurs():

    #Numérotation des capteurs de gauche à droite 
    #en se plaçant à la place du robot (pas en face)
    listeDistances = []
    

    def __init__(self):
        self.Avant1 = DistanceSensor('ds13')
        self.Avant1.enable(timestep) 

        self.Avant2 = DistanceSensor('ds14')
        self.Avant2.enable(timestep) 

        self.Avant3 = DistanceSensor('ds15')
        self.Avant3.enable(timestep) 

        self.Avant4 = DistanceSensor('ds0')
        self.Avant4.enable(timestep) 

        self.Avant5 = DistanceSensor('ds1')
        self.Avant5.enable(timestep) 

        self.Avant6 = DistanceSensor('ds2')
        self.Avant6.enable(timestep) 

        self.GaucheArriere = DistanceSensor('ds10')
        self.GaucheArriere.enable(timestep) 

        self.GaucheAvant = DistanceSensor('ds11')
        self.GaucheAvant.enable(timestep) 

        self.ArriereGauche = DistanceSensor('ds8')
        self.ArriereGauche.enable(timestep) 

        self.ArriereDroit = DistanceSensor('ds7')
        self.ArriereDroit.enable(timestep) 

        self.DroitArriere = DistanceSensor('ds5')
        self.DroitArriere.enable(timestep) 

        self.DroitAvant = DistanceSensor('ds4')
        self.DroitAvant.enable(timestep) 

        self.CoinAvantGauche = DistanceSensor('ds12')
        self.CoinAvantGauche.enable(timestep) 

        self.CoinAvantDroit = DistanceSensor('ds3')
        self.CoinAvantDroit.enable(timestep) 

        self.CoinArriereGauche = DistanceSensor('ds9')
        self.CoinArriereGauche.enable(timestep) 

        self.CoinArriereDroit = DistanceSensor('ds6')
        self.CoinArriereDroit.enable(timestep) 



    def lectureDistances(self):    
        self.listeDistances = []
        self.listeDistances.append(self.Avant1.getValue())
        self.listeDistances.append(self.Avant2.getValue())
        self.listeDistances.append(self.Avant3.getValue())
        self.listeDistances.append(self.Avant4.getValue())
        self.listeDistances.append(self.Avant5.getValue())
        self.listeDistances.append(self.Avant6.getValue())
        self.listeDistances.append(self.GaucheArriere.getValue())
        self.listeDistances.append(self.GaucheAvant.getValue())
        self.listeDistances.append(self.ArriereGauche.getValue())
        self.listeDistances.append(self.ArriereDroit.getValue())
        self.listeDistances.append(self.DroitArriere.getValue())
        self.listeDistances.append(self.DroitAvant.getValue())
        self.listeDistances.append(self.CoinAvantGauche.getValue())
        self.listeDistances.append(self.CoinAvantDroit.getValue())
        self.listeDistances.append(self.CoinArriereGauche.getValue())
        self.listeDistances.append(self.CoinArriereDroit.getValue())
        
        
        return self.listeDistances 
        
    
    
    def retourMinDistance(self):
        
        liste = self.lectureDistances()
        valeur_max = 0
        
        for i in liste: #+ la distance est petite, + le nombre est grand
            if (i > valeur_max):
                valeur_max = i
        
        #print(liste)
        print('\ndist min : ', valeur_max)
            
    
    
class monRobot(Moteurs) :
    __nom = 'El Destructor'
    
    def __init__(self):
        self.capt = Capteurs()
        self.mot = Moteurs()
        
    def run(self):
        #self.avancer()
        self.capt.retourMinDistance()
            
    
    
        

Jean_Marc = monRobot()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    
    #monRobot.reculer()
    #monRobot.turnDroite()
    #Jean_Marc.turnGauche()
    
    Jean_Marc.run()
    

    pass

