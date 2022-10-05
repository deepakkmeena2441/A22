def sumofeven(n1,n):
    if n1>n:
        return 0
    return n1+sumofeven(n1+2,n)
n=int(input("enter the number"))
n1=2
print("sum of even numbers is",sumofeven(n1,n))