from lib import pencil
def modify03(penboi):
    tot0=0
    tot1=0
    while tot0<=53:
        tot0+=1
        penboi.click()
    penboi=pencil.Pencil(int(penboi.get_num_leads())+2)
    while tot1<=15:
        tot1+=1
        penboi.click()
    return penboi
