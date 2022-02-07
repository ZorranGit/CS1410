class CaloricBalance:
    def __init__(self,gender,age,height,weight):
        self.mWeight=weight
        self.tBalance =-(self.getBMR(gender,age,height,weight))

    def getBMR(self,gender,age,height,weight):
        gender=gender.lower()
        if gender=='m':
            BMR=66+(12.7*height)+(6.23*weight)-(6.8*age)
            return BMR
        elif gender=='f':
            BMR=655+(4.7*height)+(4.35*weight)-(4.7*age)
            return BMR
        else:
            return 0

    def getBalance(self):
        return self.tBalance

    def recordActivity(self,caloric_burn,minutes):
        self.tBalance-=(caloric_burn*self.mWeight)*minutes
        return self.tBalance

    def eatFood(self,calories):
        self.tBalance+=calories
