from unit_converter.converter import convert

def test_numerical():
    converted = convert(1, "km", "m")
    assert str(converted) == "1000.0 meter"

def test_exponential():
    converted = convert(1, "km", "m", "exponential")
    assert str(converted) == "1.00e+03 meter"

def test_scientific():
    converted = convert(1, "km", "m", "scientific")
    assert str(converted) == "1.00 x 10³ meter"