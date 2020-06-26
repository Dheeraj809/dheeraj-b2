def prime(a):
    if a>1:
        for i in range(2,a):
            if(a%i)==0:
                return 0
                break
            else:
                return 1
    else:
        return 1
a=int(input("enter the number"))
if(prime(a)):
    print("it is a prime number")
else:
    print("it is not a prime number")