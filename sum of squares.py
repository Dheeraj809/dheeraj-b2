def firstnat(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum
a=int(input("enter the number:"))
print(firstnat(a))