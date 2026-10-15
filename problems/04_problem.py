class Calculator:
    def sqaure(self, x):
        return x * x
    def cube(self, x):
        return x * x * x
    def sq_root(self, x):
        return x ** 0.5
    @staticmethod
    def hello():
        return "hello"

p = Calculator()
print(p.sqaure(4))  # This will print 16
print(p.cube(3))    # This will print 27
print(p.sq_root(16)) # This will print 4.0

print(Calculator.hello())  # This will print "hello" without needing an instance of the class
