'''48.Write a Python function that checks whether a passed string is
palindrome or not'''



def check_Palindrome(string):
    string== s[::-1]
    return string

	 


s=input("enter the string: ")
ans = check_Palindrome(s)

if ans:
	print("Yes")
else:
	print("No")
