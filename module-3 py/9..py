'''Q-9.Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''

#1 and 25,26,27,28,29,
def square_list():
    squares = [i ** 2 for i in range(1, 31)]
    return squares

def elements(lists):
    if len(lists) < 5:
        return "List is too short."
    else:
        return lists[:5], lists[-5:]


new_square_list = square_list()
first_5, last_5 = elements(new_square_list)

print("First 5 elements:", first_5)
print("Last 5 elements:", last_5)




