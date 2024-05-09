'''42.Write a Python program to find the highest 3 values in a dictionary'''

def highest_value(d):
    
    highest_values = [float('-inf')] * 3
    
    for value in d.values():
        
        if value > min(highest_values):
            highest_values[highest_values.index(min(highest_values))] = value
    
    return highest_values

d = {'a': 10, 'b': 10, 'c': 20, 'd': 50, 'e': 40}

values = highest_value(d)

print("The highest 3 values in the dictionary are:", values)
