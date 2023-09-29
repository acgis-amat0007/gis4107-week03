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


