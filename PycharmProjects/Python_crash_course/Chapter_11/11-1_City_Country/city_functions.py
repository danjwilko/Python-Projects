def get_city_and_country_name(city, country, population = ''):
    if population:
        details = f"{city}, {country}, {population}"
    else:
        details = f"{city}, {country}"
    return details.title()
