from random import randint
from Exo1_file import Robot
from Exo2_Human import Human

class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        self.name = name
        self.sexe = sexe

    def resume_c(self):
        print("\nVoici un resume du Cyborg : \n")
        print("Le Cyborg s'appelle %s"%(cyborg.name))
        print("Le Cyborg est %s"%(cyborg.current_state))
        print("\n")

######### Main  #############

cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charging()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()
cyborg.resume_c()