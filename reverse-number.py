def reverseNum(x):
    is_neg=x<0
    original = abs(x)
    rev=0
    while original>0:
        digit=original%10
        rev=rev*10+digit
        original=original//10

    if is_neg:
        return -rev
    return rev
    

print(reverseNum(1234))
print(reverseNum(-1234))

#Time Complexity = number of digits = O(log10(n))
#Space Complexity = O(1)