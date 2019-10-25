from typing import List

""" Przykład serializacji i deserializacji danych, do/z json, zapisanego do pliku, zawierającego typ listy"""

"""
    Można ew. sprawdzić również (dla bardziej skomplikowanych obiektów):
    - https://json-tricks.readthedocs.io/en/latest/
    - http://jsonpickle.github.io/
"""

class U:
    def __init__(self, id, ii: List):
        self.id = id
        self.ii = ii


u = U(1,[1,2,3])
# print(u.ii)

import json

with open('data.json', 'w') as f:
    json.dump(u.__dict__, f)

with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(loaded)
    uu = U(**loaded)
print(uu.ii)