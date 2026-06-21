li=[7,1,5,3,6,4]
n=len(li)
ans=0
for i in range(n):
    for j in range(i+1,n):
      print(li[i],li[j])
      temp=li[j]-li[i]
      ans=max(ans,temp)
print(ans)