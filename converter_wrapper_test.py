#print({EXPECTED VALUE})
#print({VALUE CALLED UPON BY CONVERTER_WRAPPER})
#DO FOR EACH OF THE 9 EXAMPLES
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
    expected = "100 km/h = 27.77 m/s"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

def test_sqmeters_to_hectares():
    sqm = 10000
    actual = cw.sqmeters_to_hectares(sqm)
    expected = "10000 square metre = 1.0 hectares"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")


def test_sqmeters_to_acres():
    sqm = 10000
    actual = cw.sqmetres_to_acres(sqm)
    expected = "10000 sqm = 2.4709661477637757 ac"
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")



