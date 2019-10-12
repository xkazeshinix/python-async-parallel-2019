list1 = ['physics', 'chemistry', 1997, 2000]

# print(list1)
# for el in list1:
#     print(f'---[{el}]---')

# for i in range(10):
#     print(i)
#
# print(list1[1:])
#
# w = [i * 2 for i in range(10)]
# print(w)

# ll = [[0, 1, 2],
#       [2, 3, 4]]
# print(ll)
# print(ll[0][2])

# utworzyć talicę 2d, gdzie tab[x][y] = 2*x + y ; gdzie x=[0..10), y=[0..10);
# wydrukować tą tablicę

# podwójne pętle..
# ddd = []
# for x in range(10):
#     print(f'zaczynam prace dla x={x}')
#     for y in range(10):
#         print(2 * x + y)
#         ddd.append(2 * x + y)
#     print(f'kończę pracę dla x={x}')
# print(ddd)

# tworzenie listy składającej się z 10ciu pustych list
# zzz = []
# for x in range(10):
#     zzz.append([])
# print(zzz)


tab = []
for x in range(10):
    tmp = []
    for y in range(10):
        tmp.append(2 * x + y)
    tab.append(tmp)
print(tab)

ttab = [[2 * x + y for y in range(10)] for x in range(10)]
print(ttab)

print(tab.__len__())  # liczba elementów w liście `tab`
print(tab[0].__len__())  # liczba elementów w liście `tab[0]`

ww = [3, 6, 1, 2, 3, 4]
ww.sort()
print(ww)
