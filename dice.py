import random  #importing inbuilt module random

class dice():
    
    player_no = 0
    
    def __init__(self,name):
        self.name = name
        dice.player_no += 1
        self.player_no = dice.player_no
        
    def rolldice(self):
        self.roll = random.randint(1,7)
        with open('log.txt','a') as fl:
            fl.write(' \n '+str(self.player_no)+' '+str(self.roll)+' '+self.name)
        print(self.roll)
#checking
