'''23.Write a Python program to reverse a tuple.'''

def rev_tup(t):

    new_tup=t[::-1]
    return new_tup

tup=(1,2,3,4,5)
new_tup=rev_tup(tup)
print("the reverse tuple is :",new_tup)

