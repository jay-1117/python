'''19.Write a Python program to convert a tuple to a string.'''

def convertstr(char):

    newstr=""

    for i in char:
        newstr+=i

    return newstr

character =('h','e','l','l','o')

newstring=convertstr(character)
print("new string is :",newstring)


