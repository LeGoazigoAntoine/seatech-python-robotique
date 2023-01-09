from random import randint
from Exo1_file import Robot
from Exo2_Human import Human

class Cyborg(Robot, Human):   
    pass
# ---------------------------------------------
# Main
# ---------------------------------------------
if __name__ =='__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.changePayloadStatus()
    del cyborg