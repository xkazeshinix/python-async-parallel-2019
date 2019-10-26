"""
Klasa Car ,
pola: producer: str, model: str, year: int, milage: int
dodać konstruktor
dodać sensowny __str__
dodać metodę "cheat_milage", która pozwoli cofnięcie licznika o `param` km, default 1000km
"""
from attr import dataclass


class Car:
    def __init__(self, producer='Generic', model='Standard', year=2000, mileage=100000):
        self.producer = producer
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f'Car[{self.producer}, {self.model}, year: {self.year}, {self.mileage}km]'

    def cheat_milage(self, param=1000):
        self.mileage -= param
        self.mileage = max(self.mileage, 0)  # by nie było ujemnego stanu licznika


class ElectricCar(Car):
    def __init__(self, battery_capacity: int, producer='Generic', model='Standard', year=2000, mileage=100000):
        super().__init__(producer, model, year, mileage)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f'ElectricCar[{self.producer}, {self.model}, year: {self.year}, {self.mileage}km, ' \
               f'battery:{self.battery_capacity}]'


# smart = Car(producer='XCN')  # Auto z podanym producentem i defaultowymim pozostałymi własnościami
# nice_car = Car(producer='Xio', model='Nice', year=2020, mileage=0)  # nówka
# generic_car = Car()
# print(smart)
# smart.cheat_milage()
# print(smart)  # 99000
# smart.cheat_milage(9000)
# print(smart)  # 90000

# tworzenie auta elektrycznego
blacar = Car('KIA')
electra1 = ElectricCar(1000, 'Volvo')
print(electra1)
# print(blacar)
print(electra1.__dict__)


# zapisywanie auta jako .json do pliku
import json

with open('data1.json', 'w') as file:
    json.dump(electra1.__dict__, file)

# odczytywanie z pliku
with open('data1.json', 'r') as file_:
    dict = json.load(file_)
    print(dict)
    kopia = ElectricCar(**dict)
    print(kopia)
