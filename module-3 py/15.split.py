'''15.Write a Python program to split a list into different variables. '''

def split_list(lists):
    first=lists[0]
    second=lists[1:-1]
    return first,second
    

list1=[1,2,3,4,5]

first,second=split_list(list1)

print(first)
print(second)
