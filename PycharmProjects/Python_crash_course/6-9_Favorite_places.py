# Dictionary containing a list of places.
favorite_places = {
    'bob': ['Spain', 'Italy'],
    'lisa': ['Belguim'],
    'phil': ['France', 'Switzerland']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")

