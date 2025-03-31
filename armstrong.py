def isArmstrong(x):
    num_str=str(x)
    power=len(num_str)
    total=0
    temp=x
    while temp>0:
        digit=temp%10
        total=total+(digit**power)
        temp=temp//10

    return total==x

print(isArmstrong(153))
print(isArmstrong(9474))
print(isArmstrong(123))
print(isArmstrong(370))
print(isArmstrong(1))

#Time Complexity = O(log(n))
#Space Complexity = O(1)