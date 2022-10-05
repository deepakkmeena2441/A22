n=int(input("how many term of you want to print"))
n1=0
n2=1
if n==1:
    print(n1,end=" ")
elif n==2:
    print(n1,n2,end=" ")
else:
    print(n1,n2,end=" ")
    i=3
    while i<=n:
        c=n1
        n1=n2
        n2=c+n1
        print(n2,end=" ")
        i+=1

