# Lists
# A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [] and can contain elements of different data types, including strings, numbers, booleans, and even other lists.


dogs = ["Roger", 1, "Fido", True, 3.14]
print(dogs) # this will print the entire list: ['Roger', 1, 'Fido', True, 3.14]
print(dogs[0]) # this will print the first element of the list: Roger
print(dogs[1]) # this will print the second element of the list: 1

print("Roger" in dogs) # this will return True because "Roger" is present in the list
print("Buddy" in dogs) # this will return False because "Buddy" is not present in the list  
dogs[2] = "Buddy" # this will change the third element of the list from "Fido" to "Buddy"
print(dogs) # this will print the updated list: ['Roger', 1, '
# Buddy', True, 3.14]

# print(dogs[-2])
# print(len(dogs))

dogs.append("Max") # this will add "Max" to the end of the list
print(dogs) # this will print the updated list: ['Roger', 1, '
# Buddy', True, 3.14, 'Max']
# dogs.insert(1, "Charlie")  this will insert "Charlie" at index 1 (second position) of the list
# print(dogs) # this will print the updated list: ['Roger', 'Charlie',
# 1, 'Buddy', True, 3.14, 'Max']
# dogs.remove(1) this will remove the first occurrence of 1 from the list
# dogs.remove("Fido") this will remove the first occurrence of "Fido" from the list
# dogs.remove("Charlie") this will remove the first occurrence of "Charlie" from the list
# print(dogs) # this will print the updated list: ['Roger', 'Charlie', 'Buddy', True, 3.14, 'Max']
# dogs.pop() this will remove and return the last element of the list
# print(dogs) # this will print the updated list: ['Roger', 'Charlie', 'Buddy', True, 3.14]
# dogs.pop(1) this will remove and return the element at index 1 (second

# dogs.extend(["Charlie", "Max"]) this will add the elements of the list ["Charlie", "Max"] to the end of the dogs list
# print(dogs) # this will print the updated list: ['Roger', 1,
# 'Buddy', True, 3.14, 'Charlie', 'Max']
# dogs.clear() this will remove all elements from the list, leaving it empty
# print(dogs) # this will print an empty list: []

# dogs += ["Charlie", "Max"] this will add the elements of the list ["Charlie", "Max"] to the end of the dogs list
# print(dogs) # this will print the updated list: ['Roger', 1,
# 'Buddy', True, 3.14, 'Charlie', 'Max']
# this is equivalent to dogs.extend(["Charlie", "Max"])

#  dogs += "Breau" this will add each character of the string "Breau" as individual elements to the end of the dogs list
# print(dogs) # this will print the updated list: ['Roger', 1, 'Buddy', True, 3.14, 'Charlie', 'Max', 'B', 'r', 'e', 'a', 'u']

# items = ["Roger", 1, "Buddy", True, 3.14]

# items[1:1] = ["Charlie", "Max"] # this will insert the elements "Charlie" and "Max" at index 1 (second position) of the list
# print(items) # this will print the updated list: ['Roger', 'Charlie', 'Max
# items.insert(2, "Charlie") # this will insert "Charlie" at index 2 (third position) of the list
# print(items) # this will print the updated list: ['Roger', 1, 'Charlie

# Sorting of lists
# items.sort() # this will sort the list in ascending order (for numbers) or alphabetically (for strings)
# print(items) # this will print the sorted list: [1, 3.14
# 'Buddy', 'Roger']
# items.sort(reverse=True) # this will sort the list in descending order (for numbers)
# print(items) # this will print the sorted list: ['Roger', 'Buddy', 3.14, 1]

# note: does not sort lists that contain both numbers and strings, it will raise a TypeError: '<' not supported between instances of 'str' and 'int'
# sort list in alphabetical order
# items.sort(key=str.lower) # this will sort the list alphabetically, ignoring case
# print(items) # this will print the sorted list: ['Buddy', 'Roger']

# sorting list without modifying the original list
# sorted_items = sorted(items, key=str.lower) # this will return a new sorted list without modifying the original list
# print(sorted_items) # this will print the sorted list: [1, 3.
# 14, 'Buddy', 'Roger']



