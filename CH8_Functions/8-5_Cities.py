def describe_city(city='Reykjavik', country='Iceland'):
    print("{0} is in {1}.".format(city.title(), country.title()))

describe_city()
describe_city(country='malaysia', city='kuala lumpur')
describe_city('beijing', 'china')