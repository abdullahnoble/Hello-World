a={}
b=input().split()
for i in range(len(b)):
    if b[i] in a:
        a[b[i]]+=1
    else:
        a[b[i]]=1
print(a)
