"""Creates functions from assignment 1 exercises"""
import math


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

def sqmeters_to_hectares(sqm_3):
    """Converts square meters to hectares"""
    SQM_TO_HA = 0.0001
    ha = sqm_3*SQM_TO_HA
    return sqm_3, ha

def sqmetres_to_acres(sqm_4):
    """Converts square meters to acres"""
    SQM_TO_AC = 4047
    ac = sqm_4/SQM_TO_AC
    return sqm_4, ac

def acres_to_edge_of_square(ac2):
    """Calculates perimeter of a square acres in meters"""
    AC_TO_SQM = 4046.86
    sqm5 = ac2 * AC_TO_SQM
    lin_m = math.sqrt(sqm5)
    perim = 4*lin_m
    return ac2, perim

def get_bear_count(bear_per_sqkm, sqm6):
    """Calculates estimated number of bears of sample density in a given area"""
    sqkm = sqm6/1000000
    prb_bear = bear_per_sqkm * sqkm
    return bear_per_sqkm, sqm6, prb_bear

def dms_to_dd(deg7, min7, sec7):
    """Converts Degrees:Minutes:Seconds to Decimel Degrees"""
    dd7=deg7+(min7/60)+(sec7/3000)
    dd7=round(dd7,5)
    return deg7, min7, sec7, dd7

def dd_to_dms(dd8):
    """Converts Decimel Degrees to Degrees:Minutes:Seconds"""
    deg8 = int(dd8)
    min8 = int((dd8-deg8)*60)
    sec8 = ((dd8-deg8-min8/60)*3600)
    sec8 = round(sec8,4)
    return deg8, min8, sec8, dd8

def get_fuel_cost(km9, mpg9, cad_per_l):
    """Calculates fuel cost for a given distance at a given milage and fuel cost"""
    KM_TO_MI=0.621371
    mi = km9*KM_TO_MI
    GAL = mi/mpg9
    L_PER_GAL = 3.78541
    CAD_PER_GAL = cad_per_l * L_PER_GAL
    cost = round(GAL * CAD_PER_GAL,2)
    return km9, mpg9, cad_per_l, cost