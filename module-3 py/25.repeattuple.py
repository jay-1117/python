'''25.Write a Python program to find the repeated items of a tuple'''


def repeated_item(item):
    tup=[]

    for i in item:

        if item.count(i) > 1 and i not in tup:
            tup.append(i)
    return tuple(tup)

tup=(1,2,3,4,1)

new_tup=repeated_item(tup)

print(new_tup)
    
