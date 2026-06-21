r=6
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end='')
        #instead of this use in place of r r-1,-1,-1
    #emp=i*2+1
   # for l in range(emp):
   #     print("-",end='')
    #    break
    temp=2*r-i*2-1
    for k in range(temp):
        print("*",end='')
    print()