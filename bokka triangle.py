r=8

for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        if k==0 or k==i*2 or i==7:
           print("*",end='')
        else:
           print(" ",end="")
    print()