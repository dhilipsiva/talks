"""
class ClassName(BaseClass):
    def __init__(self):
        pass
"""

HUMAN_COLOR = "All color gradient of humans"


class Animal:
    def __init__(self, limbs, color):
        self.limbs = limbs
        self.color = color


class Person(Animal):
    def __init__(self, name, limbs=4):
        self.name = "dhilipsiva"
        super(Person, self).__init__(limbs, HUMAN_COLOR)


ds = Person("dhilipsiva")
print(ds.name)
print(ds.limbs)
print(ds.color)
