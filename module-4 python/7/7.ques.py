'''7.Write a Python program to read a file line by line store it into a variable.'''
file = open("check.txt","w")
file.write("This is line 1\n")
file.write("This is line 2\n")

file.close()
print("")

n = ""

with open("check.txt", "r") as file:
    for i in file:
        n += i

print("Print variable data")
print("\n")
print(n)
