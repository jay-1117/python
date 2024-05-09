'''10.Write a Python function that takes a list and returns a new list with
unique elements of the first list'''


def unique_elements(lists):
    unique_list = []
    for i in lists:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
        
original_list = [1, 2, 3, 3,4,5,6,7,7,8,9,10]
unique_elements = unique_elements(original_list)
print("Original list:", original_list)
print("unique elements:", unique_elements)
