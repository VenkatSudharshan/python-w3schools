def reverseArray(arr):
    rev_arr=[]
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    return rev_arr

print(reverseArray([1,2,3,6,3,2]))
