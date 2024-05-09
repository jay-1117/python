'''32.Write a Python script to check if a given key already exists in a
dictionary.'''


def check_key(d, key):
    if key in d:
        print("Key already exists")
    else:
        print("Key does not exist")

d1 = {1: "a", 2: "b", 3: "c"}
key_to_check = int(input("enter the key: ",))

check_key(d1, key_to_check)


            

    
