"""Creates functions from assignment 1 exercises"""

def miles_to_km(miles):
    """Converts miles to kilomeeters"""
    MI_TO_KM = 1.609
    kilometers = MI_TO_KM * miles
    return miles, kilometers

def km_per_hr_to_m_per_s(kph):
    """Converts kilometers per hour to meters per second""" 
    KPH_TO_MPS = 0.27777777
    mps=kph*KPH_TO_MPS
    return kph, mps   

def sqmetres_to_hectares(sqm_3):
    """Converts square meters to hectares"""
    SQM_TO_HA = 0.0001
    ha = sqm_3*SQM_TO_HA
    return sqm_3, ha

def sqmetres_to_acres(sqm_4):
    """Converts square meters to acres"""
    SQM_TO_AC = 4047
    ac = sqm_4/SQM_TO_AC
    return sqm_4, ac

