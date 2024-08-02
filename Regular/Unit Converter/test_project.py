from project import convert_length, convert_weight, convert_volume, convert_temp

def test_convert_length():
    assert convert_length('meter', 'kilometer', 123456) == 123.456
    assert convert_length('meter', 'decimeter', 2389) == 23890.0

def test_convert_temp():
    assert convert_temp('celsius', 'kelvin', 27) == 300.15
    assert convert_temp('fahrenheit', 'rankine', 23) == 482.67

def test_convert_weight():
    assert convert_weight('gram', 'kilogram', 3478) == 3.478
    assert convert_weight('centigram', 'hectogram', 123456789) == 12345.6789

def test_convert_volume():
    assert convert_volume('liter', 'kiloliter', 9832) == 9.832
    assert convert_volume('milliliter', 'deciliter', 24680) == 246.80000000000004
