# Dictionaries
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are defined using curly braces {} and the key-value pairs are separated by commas. The keys and
# values can be of any data type, and the values can be duplicated, but the keys must be unique.  

# Creating a dictionary

# my_dict = {"name": "Uwaish", "age": 22, "city": "New York"}
# print(my_dict) # this will print the entire dictionary: {'name': 'Uwaish', 'age': 22, 'city': 'New York'}
# print(my_dict["name"]) # this will print the value associated with the key "name": Uwaish
# print(my_dict["age"]) # this will print the value associated with the key "age": 22
# print(my_dict["city"]) # this will print the value associated with the key "city": New York
# print("name" in my_dict) # this will return True because "name" is a key in the dictionary
# print("country" in my_dict) # this will return False because "country" is
# not a key in the dictionary

# my_dict["name"] = "Khan" # this will change the value associated with
# the key "name" from "Uwaish" to "Khan"
# print(my_dict) # this will print the updated dictionary: {'name': 'Khan', 'age': 22, 'city': 'New York'}
# my_dict["country"] = "USA" # this will add a new key-value pair to the dictionary with the key "country" and the value "USA"
# print(my_dict) # this will print the updated dictionary: {'name': 'Khan ', 'age': 22, 'city': 'New York', 'country': 'USA'}
# del my_dict["age"] # this will remove the key-value pair with the key "
# age" from the dictionary
# print(my_dict) # this will print the updated dictionary: {'name': 'Khan
# ', 'city': 'New York', 'country': 'USA'}
# my_dict.clear() # this will remove all key-value pairs from the dictionary, leaving it
# empty
# print(my_dict) # this will print an empty dictionary: {}

# print(my_dict.get("name")) # this will return the value associated with the key "name": Khan
# print(my_dict.get("age")) # this will return None because the key "age" has been deleted from the dictionary
# print(my_dict.get("age", "Not found")) # this will return "Not found" because the key "age" has been deleted from the dictionary and we have provided a default value to return when the key is not found

# pop method removes the key-value pair with the specified key and returns the value associated with that key. If the key is not found, it raises a KeyError unless a default value is provided.
# print(my_dict.pop("name")) # this will remove the key-value pair with the key
# "name" from the dictionary and return the value "Khan"
# print(my_dict) # this will print the updated dictionary: {'city': 'New York', 'country': 'USA'}
# print(my_dict.pop("age", "Not found")) # this will return "Not found" because the key "age" has been deleted from the dictionary and we have provided a default value to return when the key is not found
# print(my_dict) # this will print the unchanged dictionary: {'city': 'New York', 'country': 'USA'}
# print(my_dict.popitem()) # this will remove and return an arbitrary key-value pair from the dictionary as a tuple (key, value)
# print("country "in my_dict) # this will return False because the key "country" has been removed from the dictionary by the popitem() method   

# this method is useful for iterating over the dictionary and modifying it at the same time, as it allows you to remove items from the dictionary while iterating without causing a RuntimeError: dictionary changed size during iteration.
# print(list(my_dict.keys())) # this will return a list of all the keys in the dictionary: ['city']
# print(list(my_dict.values())) # this will return a list of all the values in the
# dictionary: ['New York']
# print(list(my_dict.items())) # this will return a list of all the key-value pairs in the dictionary as tuples: [('city', 'New York')] 

# copy of a dictionary
# my_dict_copy = my_dict.copy() # this will create a shallow copy of the dictionary 
# print(my_dict_copy) # this will print the copied dictionary: {'city': 'New York'}
# my_dict_copy["city"] = "Los Angeles" # this will change the value associated
# with the key "city" in the copied dictionary from "New York" to "Los Angeles"
# print(my_dict_copy) # this will print the updated copied dictionary: {'city': '
# Los Angeles'}
# print(my_dict) # this will print the original dictionary: {'city': 'New York'} because the original dictionary is not affected by changes made to the copied dictionary
