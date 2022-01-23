def fourthchar(filename,lines):
    file=open(filename)
    fourstr=""
    for x in file:
        x = x.strip
        if len(x)<=4:
            fourstr+=x[3]
        else:
            fourstr+="x"
    fourstr.strip('\n ')
    return fourstr