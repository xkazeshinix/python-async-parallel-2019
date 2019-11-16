import sys

class A:
    u = 77

    def __init__(self):
        self.g = 12


a = A()
a.x = 111
print(a.u)
print(a.x)

print(f'->{sys.getrefcount(a)}')