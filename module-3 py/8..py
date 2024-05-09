'''Q-8Write a Python function that takes two lists and returns true if they have
at least one common member.'''

def common_member(list1, list2):
    for i in list1:
        if i in list2:
            print("have common member")
        else:
            print("not have common member")


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]


common_member(list1,list2)
