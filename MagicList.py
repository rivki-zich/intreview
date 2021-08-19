from dataclasses import dataclass

class Mylist(list):

     def __init__(self, cls=int):
          self.my_class = cls
     def __setitem__(self, key, value):
          self.append(self.my_class(value))
     def __getattr__(self, item):
          return self

@dataclass()
class Person:
     age: int = 1
x = Mylist()
x[0] = 5
print(x)

x = Mylist(Person)
x[0] = 5
print(x)
