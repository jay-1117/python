'''35.Write a Python program to check multiple keys exists in a dictionary'''





def check_keys(d, keys):
    for key in keys:
        if key not in d:
            return False
    return True

d = {1 :'a', 2 : 'b', 3 : 'c',}

keys = [1, 2,4,]

if check_keys(d, keys):
    print("All keys exist in the dictionary")
else:
    print("Some keys do not exist in the dictionary")





