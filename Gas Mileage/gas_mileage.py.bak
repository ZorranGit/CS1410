import sys
def milesPerGallon(miles,gallons):
    if gallons==0 or miles==0:
        return float()
    else:
        return float(miles/gallons)

def createNotebook():
    notebook=[]
    return notebook

def recordTrip(notelist,date,miles,pumped):
    dictboi={'date': date, 'miles': miles, 'gallons': pumped}
    notelist.append(dictboi)
    
def listTrips(notelist):
    stringboi=[]
    for i in notelist:
        miles=i['miles']
        gallons=i['gallons']
        date=i['date']
        milespos=milesPerGallon(miles,gallons)
        string="On {0}: {1} miles traveled using {2} gallons. Gas mileage: {3} MPG".format(date,str(miles),str(gallons),str(milespos))
        stringboi.append(string)
    return stringboi

def calculateMPG(notelist):
    miles=0
    gallons=0
    for i in notelist:
        miles+= i['miles']
        gallons += i['gallons']
    return milesPerGallon(miles,gallons)


def formatMenu():
    menulist=['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    return menulist

def formatMenuPrompt():
    return "Enter an option: "

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
                print ("Enter a valid float number")
        except:
            print ("Enter a valid float number")
            
def getDate():
    date=getUserString('Date: ')
    return date

def getMiles():
    miles=getUserFloat('Miles : ')
    return miles

def getGallons():
    gallons=getUserFloat('Gallons: ')
    return gallons

def recordTripAction(notelist):
    date=getDate()
    miles=getMiles()
    gallons=getGallons()
    recordTrip(notelist, date, miles, gallons)
    print ('Trip log was saved')
    
def listTripsAction(notelist):
    trips=listTrips(notelist)
    if not trips:
        print ("There are no trips")
    for i in trips:
        print (i)

def calculateMPGAction(notelist):
    if not notelist:
        print ("There is no trip date")
    else:
        mpg=calculateMPG(notelist)
        print("Average MPG" + str(mpg))
        
def quitAction(notelist):
    print ('End')
    sys.exit( 0 )
    
def applyAction(notelist,string):
    if string=='r':
        recordTripAction(notelist)
    elif string=='l':
        listTripsAction(notelist)
    elif string=='c':
        calculateMPGAction(notelist)
    elif string=='q':
        quitAction(notelist)
    else:
        print ("That is not a valid option")
        
def main():
    notelist=createNotebook()
    menu=formatMenu()
    while True:
        for i in menu:
            print (i)
        input1=getUserString(formatMenuPrompt())
        applyAction(notelist, input1)
    return

if __name__=='__main__':
    main()




