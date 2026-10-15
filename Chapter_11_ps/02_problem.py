class Animals:
    def __init__(self, name):
        self.name = name

class pet(Animals):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

class Dog(pet):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    @staticmethod
    def bark():
        return "Woof!"

a = Animals("Generic Animal")
print(a.name)

p = pet("Buddy", "Dog")
print(p.name)

d = Dog("Max", "Dog", "Golden Retriever")
print(d.name)
print(d.bark())