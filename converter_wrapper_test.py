import converter_wrapper as cw

def test_miles_to_km():
    miles = 10 
    actual = cw.miles_to_km(miles)
    expected = "10 miles = 16.09 kilometers"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_km_per_hr_to_m_per_s():
    kph=100
    actual = cw.km_per_hr_to_m_per_s(kph)
    expected = "100 km/h = 27.78 m/s"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_sqmeters_to_hectares():
    sqm = 10000
    actual = cw.sqmeters_to_hectares(sqm)
    expected = "10000 square meters = 1.0 hectares"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")


def test_sqmeters_to_acres():
    sqm = 10000
    actual = cw.sqmetres_to_acres(sqm)
    expected = "10000 sqm = 2.4709661477637757 ac"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_acres_to_edge_of_square():
    ac = 2
    actual = cw.acres_to_edge_of_square(ac)
    expected = "Edge length of 2 acres square is 359.86 meters"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_get_bear_count():
    bear_per_sqkm = 4
    sqm = 10000000
    actual = cw.get_bear_count(bear_per_sqkm,sqm)
    expected = "When bear density is 4 bears/sq. km, and the area is 10000000 sq. m, the probable number of bears is 40"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_dms_to_dd():
    deg = 95
    min = 25
    sec = 5
    actual = cw.dms_to_dd(deg,min,sec)
    expected = "95:25:5 = 95.41806"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_dd_to_dms():
    dd = 95.41805
    actual = cw.dd_to_dms(dd)
    expected = "95.41805 = 95:25:4.98"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_get_fuel_cost():
    km = 100
    mpg = 35
    cad_per_l = 1.30
    actual = cw.get_fuel_cost(km, mpg, cad_per_l)
    expected = "100 km at 35 mi/gal and $ 1.3 per L will cost $8.74"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

test_miles_to_km()
test_km_per_hr_to_m_per_s()
test_sqmeters_to_hectares()
test_sqmeters_to_acres()
test_acres_to_edge_of_square()
test_get_bear_count()
test_dms_to_dd()
test_dd_to_dms()
test_get_fuel_cost()






