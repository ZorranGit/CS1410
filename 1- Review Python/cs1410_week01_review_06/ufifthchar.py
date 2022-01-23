def fifthchar(filename):
    file = open(filename)
    fivestr = ''
    for x in file:
        x = x.strip()
        if len(x) >= 5:
            fivestr += x[4]
        else:
            pass
    fivestr.strip('\n ')
    return fivestr