import converter


def miles_to_km(miles):
    "Returns result of miles to kilometers as sentance "
    result1 = converter.miles_to_km(miles)
    return f"{result1[0]} miles = {result1[1]} kilometers"

def km_per_hr_to_m_per_s(kph):
    """Returns result of kilometers per hour to meters per second"""
    result2 = converter.km_per_hr_to_m_per_s(kph)
    return f"{result2[0]} km/h = {result2[1]} m/s"

def sqmeters_to_hectares(sqm_3):
    """Returns result of square meters to hecatares"""
    result3 = converter.sqmeters_to_hectares(sqm_3)
    return f"{result3[0]} square meters = {result3[1]} hectares"

def sqmetres_to_acres(sqm_4):
    """Returns result of square meters to acres"""
    result4 = converter.sqmetres_to_acres(sqm_4)
    return f"{result4[0]} sqm = {result4[1]} ac"

def acres_to_edge_of_square(ac2):
    """Returns result of perimeter of square acres"""
    result5 = converter.acres_to_edge_of_square(ac2)
    return f"Edge length of {result5[0]} acres square is {round(result5[1],2)} meters"

def get_bear_count(bear_per_sqkm, sqm6):
    """Returns estimated number of bears"""
    result6 = converter.get_bear_count(bear_per_sqkm, sqm6)
    return f"When bear density is {result6[0]} bears/sq. km, and the area is {result6[1]} sq. m, the probable number of bears is {int(result6[2])}"

def dms_to_dd(deg, min, sec):
    """Returns decimal degrees from degrees, minutes, seconds"""
    result7 = converter.dms_to_dd(deg, min, sec)
    return f"{result7[0]}:{result7[1]}:{result7[2]} = {result7[3]}"

def dd_to_dms(dd):
    """Returns degrees, minute, seconds from decimal degrees"""
    result8 = converter.dd_to_dms(dd)
    return f"{result8[3]} = {result8[0]}:{result8[1]}:{result8[2]}"

def get_fuel_cost(km, mpg, cad_per_l):
    """Return cost of fuel"""
    result9 = converter.get_fuel_cost(km, mpg, cad_per_l)
    return f"{result9[0]} km at {result9[1]} mi/gal and $ {result9[2]} will cost {result9[3]}"




