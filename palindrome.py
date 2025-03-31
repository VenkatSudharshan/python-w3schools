def isPalindrome(x):
    rev=0
    original=x
    while x>0:
        digit=x%10
        rev=rev*10+digit
        x=x//10
    
    if(original==rev):
        return True
    return False

print(isPalindrome(121))
print(isPalindrome(123))
print(isPalindrome(1001))
print(isPalindrome(10))


#Time Complexity = O(log n) because number of digits in n = log10(n)
#Space Complexity = O(1)  few variables

