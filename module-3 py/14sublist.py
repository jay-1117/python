'''14.Write a Python program to check whether a list contains a sub list'''

def is_sublist(main_list, sub_list):
    # Iterate through the main list
    for i in range(len(main_list) - len(sub_list) + 1):
        # Check if the current slice of the main list matches the sublist
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False

# Example usage:
main_list = [1, 2, 3, 4, 5, 6, 7, 8]
sub_list1 = [3, 4, 5]
sub_list2 = [8, 9]

print("Is", sub_list1, "a sublist of", main_list, ":", is_sublist(main_list, sub_list1))
print("Is", sub_list2, "a sublist of", main_list, ":", is_sublist(main_list, sub_list2))

