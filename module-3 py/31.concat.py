'''31.Write a Python script to concatenate following dictionaries to create a
new one.'''

d1 = {1: "akshay", 2: "virat", 3: "jay"}
d2 = {4: "rohit", 5: "surya", 6: "tilak"}
d3 = d1.copy()
d3.update(d2)
    
print(d3)   




