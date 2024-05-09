'''26.Write a Python program to remove an empty tuple(s) from a list of tuples.'''

def remove_emty_tup(item):

    list1=[]

    for i in item:
        if i:
            list1.append(i)
        
    return list1      
            
   
        

list1=[(),(1,2,3),(1,2,3)];

new_list=remove_emty_tup(list1)

print(new_list)
