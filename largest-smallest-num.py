def largestSmallest(arr):
    largest=arr[0]
    smallest=arr[0]
    for i in range(len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
        if(arr[i]>largest):
            largest=arr[i]
    return smallest, largest

print(largestSmallest([-3,-2,-9]))

#Time Complexity = O(n)
#Space Complexity = O(1)