# class Employee:
#     company = "ABC Corp"
#     def show(self):
#         print(f"Employee: {self.name}, Salary: {self.salary}")

# class Programmer(Employee):
#     company = "XYZ Tech"
#     def show(self):
#         print(f"Programmer: {self.name}, Salary: {self.salary}, Language: {self.language}")

#     def showlanguage(self):
#         print(f"Programming Language: {self.language}") 
        
# a = Employee()
# b = Programmer()

# print(a.company)  # Output: ABC Corp
# print(b.company)  # Output: XYZ Tech

class Employee:
    company = "ABC Corp"
    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Programmer(Employee):
    company = "XYZ Tech"
    def showlanguage(self):
        print(f"Programming Language: {self.language}") 
        
a = Employee()
b = Programmer()

print(a.company)  # Output: ABC Corp
print(b.company)  # Output: XYZ Tech