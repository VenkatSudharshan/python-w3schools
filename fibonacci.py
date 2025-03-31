def fibonacci(x):
    a=0
    b=1
    for i in range(x):
        print(a, end=" ")
        a,b=b,a+b

fibonacci(3)

#time complexity = O(n)
#space complexity = O(1)