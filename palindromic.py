a=str(input("Enter a string:"))
b=len(a)
c=[]
for i in range(b):
    if(a[i]==a[-(i+1)]):
        if a[i] not in c:
            c.append(a[i])
if c==[]:
    print("No palindromic items")
else:
    print("Palindromic items from the string are:",c)
