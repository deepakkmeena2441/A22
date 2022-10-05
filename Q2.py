def sumofodd(n1,n):
    if n1>n:
        return 0
    return n1+sumofodd(n1+2,n)

n=int(input("enter the number"))
n1=1
a=sumofodd(n1,n)
print(a)

