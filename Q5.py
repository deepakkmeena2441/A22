def sumofcubes(n1,n):
    if n1>n:
        return 0
    return n1**3 +sumofcubes(n1+1,n)
n=int(input("enter the number"))
n1=1
print("sum of cubes is ",sumofcubes(n1,n))