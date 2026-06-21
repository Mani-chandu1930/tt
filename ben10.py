r=8
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end='')
    temp=2*r-i*2-1
    for k in range(temp):
        print("*",end='')
    print()
for i in range(1,r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()