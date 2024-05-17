'''5.Write a Python program to read last n lines of a file.'''

file = open("check.txt","w")
file.write("This is line1\n")
file.write("This is line2")

file.close()
print("File Written Successfully")
print("")


f = 'check.txt'
n = 5
with open("check.txt", "r") as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]

for i in last_n_lines:
    print(i.strip())
