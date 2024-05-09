
'''36.Write a Python script to merge two Python dictionaries'''


def merge_dic(d1,d2):

 
    d3=d1.copy()
    d3.update(d2)   
    return d3
    

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

mergedDict = merge_dic(d1, d2)
print("Merged dictionary:", mergedDict)
