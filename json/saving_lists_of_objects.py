import json

from examples.car import Car

cars = [Car(model=f'FastCar{i}') for i in range(1, 5)]

# zamiana listy obiektów na pojedyczny napis w formacie json
list_in_json = json.dumps([c.__dict__ for c in cars])

# write string to file
with open('data_list.json', 'w') as f:
    f.write(list_in_json)

# read string from file
with open('data_list.json', 'r') as f:
    json_string_from_file = f.readline()

# convert to list of Car objects again
list_of_dicts = json.loads(json_string_from_file)
list_of_cars_again = [Car(**dict_) for dict_ in list_of_dicts]

# eye candy...
for c in list_of_cars_again:
    print(c)
