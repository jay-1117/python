'''3. Write a Python program to append text to a file and display the text.'''

file=open("check.txt","w")
file.write("This is file write operation using python.")
file.close()
print("successfully")

file=open("check.txt","r")
print(file.read())
file.close()
file=open("check.txt","a")
file.write("This is file append operation using python.")
file.close()
