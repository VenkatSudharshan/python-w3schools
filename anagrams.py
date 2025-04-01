def isAnagram(a,b):
    str1=list(a.lower())
    str2=list(b.lower())
    l1=len(str1)
    l2=len(str2)

    if(l1 != l2):
        #print("not anagram")
        return False

    for i in range(l1):
        for j in range(l1-i-1):
            if(str1[j]>str1[j+1]):
                temp=str1[j]
                str1[j]=str1[j+1]
                str1[j+1]=temp
    for i in range(l2):
        for j in range(l2-i-1):
            if(str2[j]>str2[j+1]):
                temp=str2[j]
                str2[j]=str2[j+1]
                str2[j+1]=temp
    #print(str1, str2)
    return (str1==str2)

print(isAnagram("Listen","Silent"))
print(isAnagram("Listen","Reddy"))

# Time Complexity = O(n**2)
# Space Complexity = O(n)