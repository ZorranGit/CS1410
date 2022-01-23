def fourthchar(filename,lines):
    out=""
    for s in lines:
        if len(s) >=4:
            out += s[3]
        else:
            out+="x"
    f=open(filename,"w")
    f.write(out+'\n')
    f.close
