class Car:
    def __init__(self):
        self.__speed = 0
    def getSpeed(self):
        return self.__speed
    def setSpeed(self,speed):
        if speed>=0 and speed<=80:
            self.__speed=speed
            return True
        else:
            return False
    def accelerate(self,delta_speed):
        if delta_speed>0.0 and self.__speed+delta_speed<80:
            self.__speed+=delta_speed
            return True
        elif self.__speed<80 and delta_speed>0.0 and self.__speed+delta_speed>80:
            self.__speed=80
            return True
        else:
            return False
