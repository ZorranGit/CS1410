def lists_to_dict(keys,values):
    count=0
    newdict={}
    for i in values:
        newdict[keys[count]]=values[count]
        print (newdict)
        count+=1
    return newdict

lists_to_dict(["a", "b"], ["13", "7" ])
