'''39.Write a Python program to print all unique values in a dictionary.'''

from collections import Counter
def unique_value(d):
    unique_vals = []
    value_counts = Counter(d.values())
    for key, count in value_counts.items(): 
        if count == 1:
            unique_vals.append(key)  
    return unique_vals 

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 4}
unique_vals = unique_value(my_dict)

print("Unique values are:", unique_vals)
