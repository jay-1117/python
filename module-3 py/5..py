'''Q-5.Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

# len is more than 2 first last charac same.

def count_string(strings):
    count = 0
    for char in strings:
        if len(char) >= 2 and char[0] == char[-1]:
            count += 1
    return count


list1 = ["python", "anaa", "akshay", "sir", "hello", "tops"]
result = count_string(list1)
print("Number of strings where the first and last character are the same:", result)
