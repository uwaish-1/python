class A:
    a = 4

o = A()
o.a = 0 
# instance attribute 'a' is created and assigned the value 0, which overrides the class attribute 'a'
print(o.a)  # This will print 0, as the instance attribute 'a' overrides the class attribute 'a'

# class attribute can still be accessed using the class name
print(A.a)  # This will print 4, as it accesses the class attribute '
