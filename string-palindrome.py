def isPalindrome(x):
    original=x
    rev_str=[]
    for i in range(len(original)-1,-1,-1):
        rev_str.append(original[i])
    
    rev="".join(rev_str)
    if(x==rev):
        return True
    return False

print(isPalindrome("racecar"))
print(isPalindrome("venkat"))


#time complexity = O(n)
#Space Complexity = O(n)