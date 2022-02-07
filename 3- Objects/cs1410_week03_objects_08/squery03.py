from lib import pencil

def query03(p):
    return p.get_num_leads()*pencil.MAX_LEAD_LENGTH + p.get_current_lead_length()
