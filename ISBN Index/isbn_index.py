import sys

def createIndex():
    indexboi={}
    return indexboi

def recordBook(index, ISBN,title):
    index[ISBN]=title
    
def findBook(index, ISBN):
    if ISBN in index:
        return index[ISBN]
    else:
        return ("")
    
def listBooks(index):
    list=[]
    string=''
    if index==False:
        return list
    else:
        i=1
        for key in index:
            string=str(i) + ") " + key + ": " + index[key] + ' \n'
            list.append(string)
            i += 1
    return list

def formatMenu():
    list=['What would you like to do?', '[r] Record a Book' , '[f] Find a Book', '[l] List all Books' , '[q] Quit']
    return list

def formatMenuPrompt():
    return "Enter an option: "

def getUserChoice(string):
    inputboi=input(string)
    inputboi=inputboi.strip()
    while not inputboi:
        inputboi=input(string)
        inputboi=inputboi.strip()
    return inputboi

def getISBN():
    return getUserChoice('Enter ISBN: ')

def getTitle():
    return getUserChoice('Enter title: ')

def recordBookAction(index):
    ISBN=getISBN()
    title=getTitle()
    recordBook(index,ISBN,title)
    
def findBookAction(index):
    ISBN=getISBN()
    display=findBook(index, ISBN)
    print("The book name is '{}'".format(display))
    
def listBooksAction(index):
    display=listBooks(index)
    if not display:
        print("No books in index")
    else:
        for i in display:
            print(i)
            
def quitAction(index):
    display="The program is donezo, gr8 workin wit ye"  #Isnt that so friendly
    print(display)
    sys.exit(0)
    
def applyAction(index, string):
    if string=='r':
        recordBookAction(index)
    elif string=='f':
        findBookAction(index)
    elif string=='l':
        listBooksAction(index)
    elif string=='q':
        quitAction(index)
    else:
        print('Please enter a option listed below')
        
def main():
    index=createIndex();
    display=formatMenu()
    prompt=formatMenuPrompt()
    while True:
        print(display)
        input1=getUserChoice(prompt)
        applyAction(index, input1.lower())
        
if __name__=='__main__':
    main()