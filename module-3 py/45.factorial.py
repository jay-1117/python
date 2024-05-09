'''45.• Write a Python function to calculate the factorial of a number (a
nonnegative integer)'''


def cal_fact(num):
    fact=1
    for i in range(1,num+1):

        fact=fact*i
    return fact
    



factorial=int(input("enter the number: "))
              
ans=cal_fact(factorial)

print(ans)              
