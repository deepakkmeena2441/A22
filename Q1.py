def sumofn(n):
    if n==1:
        return 1
    s=n+sumofn(n-1)
    return s
    


n=int(input("enter the number"))
print(sumofn(n))