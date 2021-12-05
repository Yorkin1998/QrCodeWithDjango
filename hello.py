a=int(input())
b=int(input())
c=[]
default_list=[]
for i in range(0,a):
    for j in range(0,b):
        c.append(0)
    default_list.append(c)
    c=[]
print(default_list)