

class User:
    def __init__(self, name, rank):
        # to jest konstruktor (czyli jak tworzyć instancje klasy)
        # `self` === `this`; tnz. instancja klasy
        # sposób poniżej to definiowanie pól (==zmiennych instancji)
        self.name = name
        self.rank = rank

    #definiowanie funkcji == metod klasy
    def __str__(self):
        return f'user nazwa:{self.name}, ranga:{self.rank}'

    def greet(self):
        print(f'hello {self.name}!')



u1 = User('Xi', 1)
u2 = User('Wu', 3)
u3 = User('Deng', 2)


print(u1)
print(u2)
print(u3)

u2.greet()  # uruchomienie metody klasy