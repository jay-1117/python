'''Q-4 Write a Python function to get the largest number, smallest num and sum
of all from a list'''

def sums(numbers):

    largest_num=numbers[0]
    smallest_num=numbers[0]
    totals=0
    
    for num in numbers:

        if num > largest_num:
            largest_num=num

        elif num < smallest_num:
            smallest_num=num
        totals+=num
    return largest_num,smallest_num,totals        

lists=[1,2,3,4,5]

largest,smallest,total= sums(lists)
print("Largest number is", largest)
print("Smallest number is", smallest)
print("Total of number is", total)
