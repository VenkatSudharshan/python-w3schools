def bubbleSort(n):
    l=len(n)
    for i in range(l):
        for j in range(l-i-1):
            if(n[j]>n[j+1]):
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    return n

print(bubbleSort([1,4,3,2,5]))

# Time complexity = O(n**2)
# Space complexity = O(1)