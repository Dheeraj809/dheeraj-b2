def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s= input('enter the string')
print("The original string is:")
print(s)
print("The reversed string is:")
print(reverse(s))