'''11.Write a Python program to convert a list of characters into a string.'''

def convertstr(char):

    newstr=""

    for i in char:
        newstr+=i

    return newstr

character =['h','e','l','l','o']

newstring=convertstr(character)
print("new string is :",newstring)
