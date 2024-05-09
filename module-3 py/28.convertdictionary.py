'''28. Write a Python program to convert a list of tuples into a dictionary'''

    

def Convert(tup, di):
    di = dict(tup)
    return di
     

tups = [("jigar", 1), ("jay", 2), ("akshay", 3),] 
   
dictionary = {}
print (Convert(tups, dictionary))

        
