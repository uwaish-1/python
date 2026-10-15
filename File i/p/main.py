# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# f = open("file.txt", "w")
# data = f.write("Hello, World!")
# f.close()


# u don't need to close the file if u use the with statement, it will automatically close the file after the block of code is executed
with open("file.txt") as f:
    data = f.read()
print(data)
