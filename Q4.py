def sumofsquare(n1,n):
    if n1>n:
        return 0
    return n1**2 + sumofsquare(n1+1,n)
n=int(input("enter the number"))
n1=1
print("sum of sqaure numbers is",sumofsquare(n1,n))