"""Creates functions from assignment 1 exercises"""

def miles_to_km(miles):
    """Converts miles to kilometers"""
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

def acres_to_edge_of_square():
    """Calculates edge length of a square acres in meters"""


def get_bear_count():
    """Calculates estimated number of bears of sample density in a given area"""

def dms_to_dd():
    """Converts Degrees:Minutes:Seconds to Decimel Degrees"""

def dd_to_dms():
    """Converts Decimel Degrees to Degrees:Minutes:Seconds"""

def get_fuel_cost():
    """Calculates fuel cost for a given distance at a given milage and fuel cost"""