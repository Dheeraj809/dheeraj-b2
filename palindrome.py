num=input("enter the number:")
try:
    val=int(num)
    if num==str(num)[::-1]:
        print("the given number is palindrome")
    else:
        print("the given number is not a palindrome")
except ValueError:
    print("That not a vaild number")
finally:
    print("this block is always excuted")