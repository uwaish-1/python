

with open("log.txt") as f:
    lines = f.readlines()
lineo = 1
for line in lines:
    if("python" in line):
        print("Python is present in the log file")
        print(f"Line containing 'python': {lineo}")
        break;
    lineo += 1

else:
    print("Python is not present in the log file")
