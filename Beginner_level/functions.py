# functions
# a function is a reusable block of code that performs a specific task. It allows you to organize your code into smaller, manageable pieces and promotes code reusability. Functions can take input parameters, perform operations, and return output values.   

# def greet(name):
#     return f"Hello, {name}!" # this will return a greeting message with
# the name provided as an argument when the function is called              
# print(greet("Uwaish")) # this will call the greet function with the argument "Uwaish" and print the returned greeting message: Hello, Uwaish! 
# def add(a, b):
#     return a + b # this will return the sum of a and b
# print(add(5, 3)) # this will call the add function with the arguments 5 and 3 and print the returned sum: 8   

#  def hello(name = "my friend"):
#    return f"Hello, {name}!" #  this will return a greeting message with the name provided as an argument when the function is called, if no argument is provided, it will use the default value "my friend"

# print(hello()) # this will call the hello function without any arguments and print the returned greeting message: Hello, my friend! because the default value "my friend" is used when no argument is provided
# print(hello("Uwaish")) # this will call the hello function with the argument "Uwaish" and print the returned greeting message: Hello, Uwaish! because the provided argument "Uwaish" overrides the default value "my friend"  

# def talk(phrase):
#     def say(word):
#         print(word) # this will print the word passed as an argument to the say function
#     words = phrase.split() # this will split the phrase into a list of words    
#     for word in words:
#         say(word) # this will call the say function for each word in the list of words, printing each word on a new line    

# talk("Hello, how are you?") # this will call the talk function with the argument "Hello, how are you?" and print each word in the phrase on a new line:
# # Hello,

# def count():
#     count = 0

#     def increment():
#         nonlocal count # this will allow us to modify the count variable defined in the outer function count() from within the inner function increment()
#         count += 1 # this will increment the count variable by 1 each time the increment function is called
#         print(count) # this will print the current value of count after it has been incremented
#     increment() # this will call the increment function, which will increment count to 1 and print 1

# count() # this will call the count function, which will call the increment function and print 1


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count # this will return the current value of count after it has been incremented
    return increment # this will return the increment function itself, allowing us to call it multiple times to get the updated count value each time
my_counter = counter() # this will call the counter function and assign the returned increment function to the variable my_counter
print(my_counter()) # this will call the my_counter function (which is the increment function)
print(my_counter()) # this will call the my_counter function again, which will increment count to 2 and return 2
print(my_counter()) # this will call the my_counter function again, which will increment count to