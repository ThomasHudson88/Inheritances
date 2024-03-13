
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


#Can't creat a Subclass without the Super first
#First thing is calling the supercalss
class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
