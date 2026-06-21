s="abcd"
ans=0
for i in range(len(s)-1):
    print(s[i],s[i+1])
    x=abs(ord(s[i])-ord(s[i+1]))
    ans=ans+x
print(ans)