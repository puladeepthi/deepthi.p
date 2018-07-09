a=int(input())
b=[]
c=[]
d=[]
for i in range(a):
    x=int(input())
    b.insert(i,x)
for j in range(a):
    x=int(input())
    c.insert(i,x):
d=b[::-1]
if(d==c):
  print("Yes")
else:
  print("no")
 
