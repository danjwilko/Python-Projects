cities = {
    'paris': {'country': 'france', 'population': '1.161 million', 'fact': 'Is home to the Eiffel tower'},
    'berlin': {'country': 'germany', 'population': '3.645 million', 'fact': 'Once had a dividing wall, and was split '
                                                                            'in to East and West Berlin'},
    'madrid': {'country': 'spain', 'population': '3.223 million', 'fact': 'It has a statue to for the devil in the park'}
}

for city, details in cities.items():
    country = details['country']
    population = details['population']
    fact = details['fact']

    print(f'{city.title()} is in {country.title()}, and has a population of {population} people,'
          f' {fact}.')
