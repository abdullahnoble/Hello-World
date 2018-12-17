a=[]
n=int(input("Enter number:"))
for i in range(n):
    if i==0:
        a.append(0)
    elif i==1:
        a.append(1)
    else:
        a.append(a[i-1]+a[i-2])
for i in range(n):
    print(a[i])
