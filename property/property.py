import math


class triangle:
    def __init__(self):
        self.a = 30
        self.b = 30
        self.c = math.sqrt(self.a**2 + self.b**2)

t = triangle()
t.a = 20
t.b = 25
print(t.c)


class A:
    def __init__(self):
        self.__a = 'A'
        self.__b = 'B'
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @a.setter
    def a (self, x):
        if type(x) == int:
            print('fy fy')
        else:
            self.__a = x
            
    def b(self, x):
        if isinstance(x, str):
            sel.__b = x
        else:
            print('naughty naughty')
            
a = A()

print(a.a)
a.a = 10
a.b = 10
print(a.b)



l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3= l1 + l2

print(l3)