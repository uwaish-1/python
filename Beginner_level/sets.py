# sets
# sets are unordered collections of unique elements
# creating a set
# my_set = {1, 2, 3, 4, 5}
# print(my_set) # this will print the set: {1, 2, 3, 4, 5}
# my_set = {1, 2, 3, 4, 5, 5, 5} # this will create a set with unique elements only, so the duplicate 5s will be ignored
# print(my_set) # this will print the set: {1, 2, 3, 4, 5}
# my_set = {1, 2, 3, "apple", "banana", "cherry"}
# print(my_set) # this will print the set: {1, 2, 3, 'apple', 'banana', 'cherry'}
# print(1 in my_set) # this will return True because 1 is present in the set
# print("apple" in my_set) # this will return True because "apple" is present in the set
# print("grape" in my_set) # this will return False because "grape  is not present in the set
# my_set.add("grape") # this will add "grape" to the set    
# print(my_set) # this will print the updated set: {1, 2, 3, 'apple', 'banana', 'cherry', 'grape'}
# my_set.remove(1) # this will remove 1 from the set    
# print(my_set) # this will print the updated set: {2, 3, 'apple', 'banana', 'cherry', 'grape'}
# my_set.discard(2) # this will remove 2 from the set, but              
# print(my_set) # this will print the updated set: {3, 'apple', 'banana', 'cherry', 'grape'}
# my_set.discard(4) # this will not raise an error because 4 is
# not present in the set, it will simply do nothing
# print(my_set) # this will print the unchanged set: {3, 'apple', 'banana', 'cherry', 'grape'}
# my_set.pop() # this will remove and return an arbitrary element from the set, since   sets are unordered, we cannot predict which element will be removed
# print(my_set) # this will print the updated set with one less element, but we cannot predict which element will be removed
# my_set.clear() # this will remove all elements from the set, leaving it empty 
# print(my_set) # this will print an empty set: set() because sets are defined using curly braces {}, an empty set cannot be represented by {} as it would be interpreted as an empty dictionary, so we use the set() constructor to create an empty set    

# set1 = {"roger", "syd"}
# set2 = {"syd", "breau"}

# intersect = set1 & set2 # this will return a new set containing the common elements of set1 and set2, which is {"syd"}
# print(intersect) # this will print the intersecting set: {'syd'}

# mod
# mod = set1 | set2 # this will return a new set containing all the unique elements from both set1 and set2, which is {"roger", "syd", "breau"}
# print(mod) # this will print the union of the sets: {'roger', 'syd', 'breau'}

# mod = set1 > set2 # this will return a new set containing the elements that are in set1 but not in set2, which is {"roger"}
# print(mod) # this will print the difference of the sets: {'roger'}            

# print(list(set1)) # this will convert the set to a list and print it: ['roger', 'syd']    
