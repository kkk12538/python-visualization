from random import choice

class Die():
    def __init__(self,die_num):
        self.die_num=die_num
        self.results=[]
    def rolling(self,number):
        for i in range(number):
            self.results.append(choice(list(range(1,self.die_num+1))))

