def fun(n,c):
    if n==1:
        c+=1
        return c
    elif n%2==0:
        c+=1
        return fun(n//2,c)
    else:
        c+=1
        return fun(3*n+1,c)


a,b=1,10
l=[]
for i in range(a,b+1):
    l.append(fun(i,0))
print(max(l))