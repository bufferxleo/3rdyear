#coins
c=list(map(int,input().split()))
#target
t=int(input())
a=[]
for j in range(len(c)):
    temp=[]
    for i in range(t):
        temp.append(0)
    a.append(temp)

for i in range(t):
    a[0][i]=(i+1)//c[0]

for j in range(1,len(c)):
    for i in range(t):
        a[j][i]=a[j-1][i]

for j in range(1,len(c)):
    for i in range(t):
        if i-c[j]>=0:
            a[j][i]=a[j][i-c[j]]+1
print(a)