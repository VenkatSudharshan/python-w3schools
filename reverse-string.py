def reverseString(s):
    #original=s
    temp=[]
    for i in range(len(s)-1,-1,-1):
        temp.append(s[i])
    return "".join(temp)

print(reverseString("Venkat"))

# Time complexity = O(n)
# Space complexity = O(n)
