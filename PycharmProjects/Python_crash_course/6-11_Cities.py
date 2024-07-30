cities = {
    'paris': {'country': 'france', 'population': '1.161 million'},
    'berlin': {'country': 'germany', 'population': '3.645 million'},
    'madrid': {'country': 'spain', 'population': '3.223 million'}
}

for city, details in cities.items():
    print(f"The city of {city.title()} is in {details['country'].title()} and"
          f" has a population of {details['population']} people.")
