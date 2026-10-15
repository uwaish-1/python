# Tuples

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Creating a tuple

# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple) # this will print: ('apple', 'banana', 'cherry')
# Accessing tuple items
# print(my_tuple[0]) # this will print "apple" because it is the first
# print(my_tuple[1]) # this will print "banana" because it is the second
# print(my_tuple[2]) # this will print "cherry" because it is the
# print(my_tuple[-1]) # this will print "cherry" because it is the last
# my_tuple[0] = "grape" # this will raise a TypeError: 'tuple' object does not support item assignment because tuples are immutable
# my_tuple.append("grape") # this will raise an AttributeError: 'tuple'
# my_tuple.remove("banana") # this will raise an AttributeError: 'tuple' object has no attribute 'remove' because tuples do not have methods like append() or remove() that modify the tuple

# my_tuple.index("banana") # this will return the index of the first occurrence of "banana" in the tuple, which is 1
# my_tuple.count("banana") # this will return the number of times "banana" appears
# in the tuple, which is 1
# len(my_tuple) # this will return the number of items in the tuple, which is 3

# print("apple" in my_tuple) # this will return True because "apple" is present in the tuple
# print("grape" in my_tuple) # this will return False because "grape" is not present in the tuple  


# my_tuple[0:2] # this will return a new tuple containing the items from index 0 to index 1 (not including index 2), which is ('apple', 'banana')

# sorted function in tuples
# sorted_tuple = sorted(my_tuple) # this will return a new list containing the sorted items of the tuple, which is ['apple', 'banana', 'cherry']
# print(sorted_tuple) # this will print the sorted list: ['apple', 'banana', 'cherry'] 

# new_tuple = my_tuple + ("grape", "orange") # this will create a new tuple by concatenating the original tuple with another tuple containing "grape" and "orange"
# print(new_tuple) # this will print the new tuple: ('apple', 'banana', 'cherry', 'grape', 'orange')

# note: cannot modify a tuple, but can create a new tuple by concatenating the original tuple with another tuple or by slicing the original tuple to create a new tuple.