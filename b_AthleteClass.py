
class Athlete:
    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf

#Athlete is the Super Class and Football Player is the Sub Class

class Football_Player(Athlete):

    def __init__(self,ht,wt,bodyfat,position,team):

        Athlete.__init__(self,ht,wt,bodyfat)
        #first you must call/initialize the super class when you are working with sub classes

        self.__position = position
        self.__team = team


    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
