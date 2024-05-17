'''6.Write a Python program to read a file line by line and store it into a list'''

'

file = open("check","w")
file.write("This is line 1\n")
file.write("This is line 2")

file.close()
print("")


lists = []

with open("check", "r") as file:
    for i in file:
        lists.append(i.strip())

print(lists)
