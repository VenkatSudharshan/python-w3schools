def gcd(a,b):
    smallest=min(a,b)
    gcd=1
    for i in range(1,smallest+1):
        if(a%i==0 and b%i==0):
            gcd=i
    return gcd

def lcm(a,b):
    lcm=(a*b)/gcd(a,b)
    return lcm

print(gcd(12,18))
print(lcm(12,18))

#time complexity = O(min(a,b))
#space complexity = O(1)