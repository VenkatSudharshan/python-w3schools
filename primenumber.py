def isPrime(x):
    if(x<=1):
        return False
    for i in range(2,int(x**0.5)+1):
        if(x%i==0):
            return False
    return True

print(isPrime(2))
print(isPrime(4))
print(isPrime(13))
print(isPrime(1))
print(isPrime(99))

#Time Complexity = O(x**0.5) or O(sqrt(x))
#Space Complexity = O(1) Since no data structure used
