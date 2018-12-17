from collections import OrderedDict

ord_dict=OrderedDict()
N=int(input("Enter number of items:"))
if(N>100 or N<=0):
    print("Invalid Input")
else:
    for i in range (N):
        b=input().split()
        if b[0] in ord_dict:
            ord_dict[b[0]]+=int(b[1])
        else:
            ord_dict[b[0]]=int(b[1])
print(ord_dict)
