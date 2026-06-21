
s = "aAAbbbb"
ans = 0
for i in range(len(s)):
    if s[i] == "a" or s[i] == "A":
        ans = ans + 1
print(ans)
