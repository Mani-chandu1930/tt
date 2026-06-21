li=[4,2,6,1,6]
minval=li[0]
ans=0
for i in range(1,len(li)):
    ans=max(ans,(li[i]-minval))
    minval=min(minval,li[i])
print(ans)
    