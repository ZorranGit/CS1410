import caloric_balance
import sys
def formatMenu():
    return ["What would you like to do?", "[f] Record Food Consumption", "[a] Record Physical Activity", "[q] Quit"]

def formatMenuPrompt():
    return "Enter an option: "

def formatActivityMenu():
    return ["Choose an activity to record", "[j] Jump Rope", "[r] Running", "[s] Sitting", "[w] Walking"]

def getUserString(string):
    input1=input(string)
    input1=input1.strip()
    while not input1:
        input1=input(string)
        input1=input1.strip()
    return input1

def getUserFloat(string):
    while True:
        try:
            float1=input(string)
            float1=float(float1)
            if float1 > 0.0:
                return float1
            else:
                print ("Enter a valid float number greater than or equal to 0")
        except:
            print ("Enter a valid float number greater than or equal to 0")

def createCaloricBalance():
    gender=getUserString("What is your gender?: ")
    age=getUserFloat("What is your age?: ")
    height=getUserFloat("What is your height?: ")
    weight=getUserFloat("What is your weight?: ")
    return caloric_balance.CaloricBalance(gender, age, height, weight)

def recordActivityAction(caloricBalance):
    menu=formatActivityMenu()
    prompt=formatMenuPrompt()
    for i in menu:
        print (i)
    option=getUserString(prompt)
    option=option.lower()
    if option=="j":
        number=.08
    elif option=="r":
        number=.095
    elif option=="s":
        number=0.009
    elif option=="w":
        number=0.36
    else:
        print ("Please enter a valid option: ")
        return 0
    minutes=getUserFloat("How many minutes did you exercise?: ")
    caloricBalance.recordActivity(number,minutes)
    string="Your caloric balance is now {}".format(caloricBalance.getBalance())
    print (string)

def eatFoodAction(caloricBalance):
    calories=getUserFloat("Input how many calories you consumed: ")
    caloricBalance.eatFood(calories)
    string="Your caloric balance is now {}".format(caloricBalance.getBalance())
    print (string)

def quitAction(caloricBalance):
    print ("EndBoi")
    sys.exit( 0 )

def applyAction(caloricBalance, choice):
    choice=choice.lower()
    if choice=="f":
        eatFoodAction(caloricBalance)
    elif choice=="a":
        recordActivityAction(caloricBalance)
    elif choice=="q":
        quitAction(caloricBalance)
    else:
        print ("That isnt a valid option, please enter a valid option: ")

def main():
    cB=createCaloricBalance()
    menu=formatMenu()
    prompt=formatMenuPrompt()
    while True:
        for i in menu:
            print (i)
        choice=getUserString(prompt)
        applyAction(cB, choice)

if __name__=='__main__':
    main()
