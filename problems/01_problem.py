class Programmer:
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.__pin = pin  # Private attribute
        

    def get_pin(self):
        return self.__pin
    
p = Programmer("Alice", 80000, "1234")

# print(p.__pin)  # This will raise an AttributeError because __pin is private
print(p.get_pin())  # This will correctly print the pin using the public method

print(p.name, p.salary)  # This will correctly print the name and salary