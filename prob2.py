a=["X++","X--","++X","--X"]
x=0
for i in range(len(a)):
    if a[i]=="X--" or a[i]=="--X":
        x=x-1
    else:
        x=x+1
print(x)
            