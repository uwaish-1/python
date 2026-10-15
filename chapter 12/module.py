def myFunc():
    print("Hello from myFunc!")

# myFunc()
# print(__name__) 
 # This will print "__main__" when run directly, and "module" when imported.


if __name__ == "__main__":
    # if this script is run directly, call myFunc
    print("Running 08_main.py directly.")
    myFunc()
    print(__name__) 
