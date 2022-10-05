f=lambda a:1 if a==1 else a*f(a-1)
a=int(input("enter the number"))
print("factorail of number is ",f(a))