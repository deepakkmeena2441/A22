def sumofdigit(digit,n):
    if n<1:
        return 0
    return digit +sumofdigit(digit+1,n//10)


n=int(input("enter the number"))
digit=1
print("sum of digit",sumofdigit(digit,n)) 