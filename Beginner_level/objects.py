# objects
# in Python, everything is an object, including numbers, strings, lists, functions, and even classes. An object is an instance of a class, which is a blueprint for creating objects. Each object has its own unique identity, type, and value.
a = 10
print(type(a)) # this will print <class 'int'> because a is an integer
# name = "Uwaish"
# print(type(name)) # this will print <class 'str'> because name is a string
# my_list = [1, 2, 3]
# print(type(my_list)) # this will print <class 'list'> because my_list is
# a list
# def greet():
#     return "Hello!"
# print(type(greet)) # this will print <class 'function'> because greet is a function
# class Dog:
#     def __init__(self, name): 
#         self.name = name
# my_dog = Dog("Buddy")     
# print(type(my_dog)) # this will print <class '__main__.Dog'> because my_dog is an instance of the Dog class


# objects can be mutable or immutable. Mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created. For example, lists and dictionaries are mutable, while strings and tuples are immutable.
# depends on the object type, some objects have methods that allow you to perform operations on them. For example, strings have methods like upper() and lower() that allow you to convert the string to uppercase or lowercase, while lists have methods like append() and remove() that allow you to add or remove elements from the list.

#  while loops
#  a while loop is a control flow statement that allows you to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is:
# while condition:
#     # code to be executed repeatedly
# e.g. int i = 5
# while i > 0:
#     print(i) # this will print the current value of i
#     i -= 1 # this will decrement the value of i by 1 each time the loop is executed


# for loops
# a for loop is a control flow statement that allows you to iterate over a sequence (like a list, tuple, string, etc.) and execute a block of code for each item in the sequence. The syntax for a for loop is:
# for item in sequence:     
#     # code to be executed for each item in the sequence
# e.g. for i in range(5): # this will iterate over the numbers from 0 to 4 (not including 5)
#     print(i) # this will print the current value of i in each iteration of the
# for loop

# e.g. for item in range(15):
            # print(item) # this will print the numbers from 0 to 14 (not including 15)

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     print(f"Index: {index}, Item: {item}") # this will print the index and item for each element in the items list
