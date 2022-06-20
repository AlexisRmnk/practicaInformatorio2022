def separar(city_and_quantity: list):
    cities_1 = list()
    cities_2 = list()
    for city_, quantity in city_and_quantity:
        if quantity > 100:
            cities_1.append((city_, quantity))
        else:
            cities_2.append((city_, quantity))
    return cities_1, cities_2
