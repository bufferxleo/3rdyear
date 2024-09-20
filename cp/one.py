a=list(map(int,input().split()))
c=0
maxi=0

for i in range(len(a)):
    for j in range(len(a)+1):
        c=sum(a[i:j])
        maxi=max(maxi,c)
print(maxi)


ans=0
maxi=0
for i in a:
    if ans+i<0:
        ans=0
    else:
        ans+=i
    maxi=max(maxi,ans)
print(maxi)


x=y=a[0]
for i in a[1:]:
    x=max(i,x+i)
    y=max(y,x)
print(y)


