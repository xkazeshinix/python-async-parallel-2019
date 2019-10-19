class User:
    def __init__(self, name: str, rank: int):
        # to jest konstruktor (czyli jak tworzyć instancje klasy)
        # `self` === `this`; tnz. instancja klasy
        # sposób poniżej to definiowanie pól (==zmiennych instancji)
        self.name = name
        self.rank = rank

    # definiowanie funkcji == metod klasy
    def __str__(self):
        return f'user nazwa:{self.name}, ranga:{self.rank}'

    def greet(self, second_message='', counter=0):
        print(f'Hello {self.name}! {second_message}')


def increase_rank(uu: User):
    uu.rank += 1


u1 = User('Xi', 1)
u2 = User('Wu', 3)
u3 = User('Deng', 2)

print(u1)
print(u2)
print(u3)

# increase_rank(u3)
# print(u3)

#
u2.greet()  # uruchomienie metody klasy
u2.greet(counter=12)
u2.greet(second_message='Have a good day!')


