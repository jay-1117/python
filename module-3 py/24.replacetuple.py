'''24.Write a Python program to replace last value of tuples in a list.'''

def replace(tup_list, new_value):
    new_tup_list = []
    for i in tup_list:
        
        new_tup = i[:-1] + (new_value,)
        new_tup_list.append(new_tup)
    return new_tup_list


tup = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
new_tup_list = replace(tup, new_value)
print("Original List of Tuples:", tup)
print("List of Tuples after replacing last value:", new_tup_list)

