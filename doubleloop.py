li = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans=0
for j in li:
    temp=1
    s=j
for i in range(len(s)):
    if s[i]==" ":
        temp=temp+1
    ans=max(ans,temp)
print(ans)