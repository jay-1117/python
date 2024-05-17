'''2.Write a Python program to read an entire text file'''

file=open("check.txt","w")
file.write("This is file write operation using python.")
file.close()
print("success")

file=open("check.txt","r")
print(file.read())
file.close()
