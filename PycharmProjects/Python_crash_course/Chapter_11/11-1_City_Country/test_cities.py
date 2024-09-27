from city_functions import get_city_and_country_name

def test_city_country():
    formated_details = get_city_and_country_name('San Francisco', 'America')
    assert formated_details == 'San Francisco, America'

def test_city_country_population():
    """Does adding the population parameter work"""
    formated_details = get_city_and_country_name('London', 'United Kingdom', '1000000')