'''44.Write a Python program to create a dictionary from a string'''

def dict_from_string(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


str1 = "hello"

d = dict_from_string(str1)

print("Dictionary from the string:", d)
