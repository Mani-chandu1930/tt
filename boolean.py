s="abccba"
n=len(s)//2
m=len(s)
valid=True
for i in range(n):
        l=s[m-1-i]
        r=s[i]
        if l!=r:
             valid=False
             break
if valid:
        print("yes ,its a palindrome")
else:
        print("no,its not a palindrome")

