l = [1, 2, 3, 4, 5]

# idx = 0
# for item in l:
#     print(f"Index: {idx}, Value: {item}")
#     idx+=1
#  this can be done using enumerate() function which returns both the index and the value of the item in the list


for i, value in enumerate(l):
    print(f"Index: {i}, Value: {value}")