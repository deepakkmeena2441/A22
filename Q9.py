def octalofnumber(n):
    if n==0:
        return 0
    return n%8 +10*octalofnumber(n//8)
n=int(input("enter the number"))
print("ocatal of number",octalofnumber(n))