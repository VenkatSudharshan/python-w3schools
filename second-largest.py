def secondLargest(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    l=len(arr)-2
    return arr[l]

print(secondLargest([1,3]))