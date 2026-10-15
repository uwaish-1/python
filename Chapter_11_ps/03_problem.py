class Employee:
    def __init__(self, salary, inc):
        self.salary = salary
        self.inc = inc

    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.inc / 100)

    @salary_after_increment.setter
    def salary_after_increment(self, new_salary):
        if new_salary < self.salary:
            raise ValueError("New salary cannot be less than current salary.")

        self.inc = (new_salary / self.salary - 1) * 100


e = Employee(50000, 10)

print(e.salary_after_increment)

e.salary_after_increment = 60000

print(e.salary_after_increment)
print(e.inc)