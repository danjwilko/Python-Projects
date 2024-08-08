def make_car(make, model, **veh_details):
    """Build a dictionary containing details about a car."""
    car_dict = {
        'manufacturer': make.title(),
        'model': model.title(),
    }
    for detail, value in veh_details.items():
        car_dict[detail] = value

    return car_dict


my_car = make_car('Honda', 'crv',
                  color='blue',
                  year=2007)

print(my_car)
