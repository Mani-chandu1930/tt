colors=[1,4,5,4,1]
n=len(colors)
ans=0
for i in range(n):
    for j in range(i+1,n):
        if colors[i]!=colors[j]:
            temp=abs(i-j)
            ans=max(ans,temp)
print(ans)
        
        
        