'''34.Write a Python script to print a dictionary where the keys are numbers
between 1 and 15.'''


def create_dictionary():
    my_dict = {}
    for i in range(1, 16):
        my_dict[i] = "hello"  
    return my_dict

result_dict = create_dictionary()
print(result_dict)
