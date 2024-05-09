'''7.Write a Python program to check a list is empty or not.'''

def list_empty(lists):
    if not lists:
        print("empty list")
    else:
        print("not a empty list")


empty_list = []
new= [1, 2, 3]

list_empty(empty_list)
list_empty(new)

