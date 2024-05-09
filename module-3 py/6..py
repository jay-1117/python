'''Q-6.Write a Python program to remove duplicates from a list.'''

def remove_duplicates(lists):
    new_list = []
    for item in lists:
        if item not in new_list:
            new_list.append(item)
    return new_list


lists = [1, 2, 3, 4, 2, 3]
new_list = remove_duplicates(lists)
print("List after removing duplicates:",new_list)
