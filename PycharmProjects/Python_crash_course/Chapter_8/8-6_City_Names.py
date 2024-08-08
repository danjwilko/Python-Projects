def city_country(city, country):
    """Return a formated string of the city and country."""
    return f"{city.title()}, {country.title()}"


city1 = city_country('santiago', 'chile')
print(city1)
city2 = city_country('london', 'uk')
print(city2)
city3 = city_country('chicago', 'usa')
print(city3)
