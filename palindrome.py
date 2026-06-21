s = "pttp"
n=len(s)
ans=""
for i in range(n-1,-1,-1):
    ans=ans+s[i]
if ans==s:
    print("s,its a palindrome")
else:
    print("no")
    
