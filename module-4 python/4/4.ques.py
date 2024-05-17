'''4.Write a Python program to read first n lines of a file.'''


file = open("check.txt","w")

file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.write("This is line 3.\n")

file.close()
print("File Written Successfully")


n_line=3

with open('check.txt', 'r') as file:
    for _ in range(n_line):
        line = file.readline().strip()
        if not line:
            print("no line")
            break
        print("\n",line)

