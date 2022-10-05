def binaryofdecimal(n):
    if n<1:
        return 0
    
    return  n%2 + 10*binaryofdecimal(n//2)

n=int(input("enter the number"))

print("binary of given decmial nunber",binaryofdecimal(n))

