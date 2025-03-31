def factorial(x):
    if(x<0):
        return "Undefined for negetive values"
    result=1
    for i in range(2,x+1):
        result=result*i
    return result

print(factorial(3))
print(factorial(-5))
print(factorial(0))

#Time Complexity = O(n)
#Space Complexity = O(1)  just using one variable to store data