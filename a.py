# print('hello')
x = 12
y = x * 7
# print(y)

# print(f'Wynik mnozenia to:{y}')
users = ['wu', 'xi', 'lao', 'vlod']
# print(users)

# for u in users:
#     print(u)
#     print('--')

# for i in range(1,6):
#     for j in range(1,6):
#         print(f'{i} x {j} = {i * j}')

a = 3
b = 12
c = 10

if b < a + c and a < b + c and c < a + b:
    print('Mozna stworzyc trojkat')
else:
    print('Nie mozna utworzyc trojkata')


def greet_user(u):
    print(f'Hello {u}! Nice to meet you!')


# tu juz funkcja sie skonczyla
users = ['wu', 'xi', 'lao', 'vlod']

for u in users:
    greet_user(u)
