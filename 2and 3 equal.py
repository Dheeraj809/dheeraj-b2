num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
all = num1 == num2 and num2 == num3 and num3 == num1
print ("All are equal:",all)
any = num1 == num2 or num2 == num3 or num3 == num1
print ("Any of two are equal:",any)