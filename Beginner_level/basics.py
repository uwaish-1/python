# name = 'Uwaish'
# print(isinstance(name, str))
# print(type(name) == str)

# age = 22
# print(isinstance(age, int))
# print(type(age) == int)

# we can also convert from one data type to another by using class constructors like str(), int(), float() etc.
# age = str(age)

# number = "10"
# age = int(number)
# print(isinstance(age, int))

# but python can't convert strings into integers if they contain non-numeric characters
# number = "ten"
# age = int(number) # this will raise a ValueError: invalid literal for int()   

# complex for complex numbers
# bool for boolean values True and False
# list for lists of items
# tuple for immutable lists of items
# set for unordered collections of unique items
# dict for key-value pairs of data(dictionaries)
# range for sequences of numbers(ranges)

# floor division operator // returns the quotient of the division rounded down to the nearest whole number
# 5 //2 = 2

# we can directly add strings together using the + operator, this is called string concatenation
# first_name = "Uwaish"
# last_name = "Khan"    
# full_name = first_name + " " + last_name
# print(full_name)

#  comparsion operators are used to compare values and return a boolean result (True or False)
# == equal to           
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# or operator returns True if at least one of the conditions is True
# or operator returns first value if it is truthy, otherwise it returns the second value
# a = 0
# b = 5
# result = a or b   
# print(result) # this will print 5 because 0 is falsy and 5 is truthy

#  and operator returns True only if both conditions are True
# and operator returns first value if it is falsy, otherwise it returns the second value

#  shift left operator << shifts the bits of a number to the left by a specified number of positions, filling the vacated bits with zeros
#  shift right operator >> shifts the bits of a number to the right by a specified number of positions, filling the vacated bits with the sign bit (the leftmost bit) for signed numbers or with zeros for unsigned numbers.

# in operator checks if a value is present in a sequence (like a string, list, tuple, etc.) and returns True if it is found, otherwise it returns False
# name = "Uwaish"
# print("a" in name) # this will return True because "a" is present in "Uwaish"
# print("z" in name) # this will return False because "z" is not

# is operator checks if two variables refer to the same object in memory and returns True if they do, otherwise it returns False
# a = [1, 2, 3]
# b = a
# print(a is b) # this will return True because a and b refer to the same

# ternary operator is a shorthand way of writing an if-else statement in a single line of code. It has the syntax: value_if_true if condition else value_if_false
# age = 22
# is_adult = "Yes" if age >= 18 else "No"
# print(is_adult) # this will print "Yes" because age is greater than or
# equal to 18


#  built-in strring methods are functions that are associated with string objects and can be called on them to perform various operations. Some common string methods include:

# upper() converts all characters in a string to uppercase
# lower() converts all characters in a string to lowercase      
# strip() removes any leading and trailing whitespace from a string
# split() splits a string into a list of substrings based on a specified delimiter (default
# is whitespace)
# join() joins a list of strings into a single string using a specified delimiter
# replace() replaces all occurrences of a specified substring with another substring
# find() returns the index of the first occurrence of a specified substring in a string, or -1 if the substring is not found
# count() returns the number of occurrences of a specified substring in a string
# startswith() returns True if a string starts with a specified substring, otherwise it returns False
# endswith() returns True if a string ends with a specified substring, otherwise it returns False
# capitalize() capitalizes the first character of a string and converts the rest to lowercase
# title() capitalizes the first character of each word in a string and converts the rest to lowercase
# isalpha() returns True if all characters in a string are alphabetic, otherwise it returns False
# isdigit() returns True if all characters in a string are digits, otherwise it returns False
# isalnum() returns True if all characters in a string are alphanumeric (letters and numbers), otherwise it returns False
# len() returns the number of characters in a string (including spaces)

# indexing and slicing can be used to access specific characters or substrings in a string. Indexing uses square brackets [] to access a single character at a specific position, while slicing uses the syntax [start:stop:step] to access a range of characters. The start index is inclusive, while the stop index is exclusive. The step parameter is optional and specifies the interval between characters to be accessed.
# for example:
# name = "Uwaish Khan"
# print(name[0]) # this will print "U" because it is the first character
# print(name[1:6]) # this will print "waish" because it is the substring from index 1 to index 5 (index 6 is exclusive)
# print(name[::2]) # this will print "Uaia a" because it is the substring of every second character starting from index 0
# we can also use negative indexing to access characters from the end of the string. The last character has an index of -1, the second to last character has an index of -2, and so on.
# name = "Uwaish Khan"
# print(name[-1]) # this will print "n" because it is the last character
# print(name[-5:-1]) # this will print "Khan" because it is
# the substring from index -5 to index -2 (index -1 is exclusive)

# escaping characters in strings can be done using the backslash \ character. For example, to include a double quote " in a string, we can use the escape sequence \" like this:
# quote = "She said, \"Hello!\""
# print(quote) # this will print: She said, "Hello!"
#  \n is used to create a new line in a string, and \t is used to create a tab space. For example:
# message = "Hello!\nWelcome to Python programming.\tEnjoy your learning journey!"
# print(message) # this will print:
# Hello!
# Welcome to Python programming.	Enjoy your learning journey!

# any() is a built-in function that takes an iterable (like a list, tuple, etc.) as an argument and returns True if at least one element in the iterable is truthy (i.e., evaluates to True in a boolean context), otherwise it returns False. For example:
# numbers = [0, 0, 0, 1]
# result = any(numbers)
# print(result) # this will print True because there is at least one truthy value (1) in the list

# eg. of using any() to check if a string contains any uppercase letters
# name = "uwaish khan"
# has_uppercase = any(char.isupper() for char in name)
# print(has_uppercase) # this will print False because there are no uppercase letters in the

# all() is a built-in function that takes an iterable as an argument and returns True if all elements in the iterable are truthy, otherwise it returns False. For example:
# numbers = [1, 2, 3, 4]
# result = all(numbers)
# print(result) # this will print True because all values in the list are truthy (
# 1, 2, 3, and 4 are all non-zero numbers)


# complex numbers are a type of number that consists of a real part and an imaginary part. In Python, we can create complex numbers using the built-in complex() function or by using the j suffix to indicate the imaginary part. For example:
# z1 = complex(2, 3) # this creates a complex number with real
# part 2 and imaginary part 3
# z2 = 1 + 4j # this creates a complex number with real part
# 1 and imaginary part 4
# we can perform various operations on complex numbers, such as addition, subtraction, multiplication, and

# eg. num = 2 + 3j
# num2 = complex(1, 4)
# print(num2.real, num2.imag) # this will print the real and imaginary parts of num2, which are 1.0 and 4.0 respectively
# we can also use the built-in functions abs() to get the magnitude of a complex number, and phase() from the cmath module to get the angle of a complex number in radians. For example:
# import cmath
# z = 2 + 3j
# magnitude = abs(z)
# eg. print(abs(-5.5))
# angle = cmath.phase(z)
# print(magnitude) # this will print the magnitude of z, which is approximately 3
# print(angle) # this will print the angle of z in radians, which is approximately 0.982793723247329

# print(round(3.14159, 2)) # this will print 3.14 because it rounds the number to 2 decimal places

# enum is a built-in module that provides a way to define and use enumerations in Python. An enumeration is a set of symbolic names (members) bound to unique, constant values. We can define an enumeration by subclassing the Enum class from the enum module and defining the members as class attributes. For example:
# from enum import Enum
# class Color(Enum):
#     RED = 1   
#     GREEN = 2
#     BLUE = 3
# we can access the members of the enumeration using their names or values. For example:
# print(Color.RED) # this will print Color.RED
# print(Color.GREEN.value) # this will print 2
# we can also iterate over the members of an enumeration using a for loop. For example:
# for color in Color:
#     print(color) # this will print each member of the Color enumeration (Color.RED, Color.GREEN, and Color.BLUE)

