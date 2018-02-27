def make_car(model, region, **features):
    car_type = {}
    car_type['Model'] = model
    car_type['Region'] = region
    for key, value in features.items():
        car_type[key] = value
    return  car_type

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)