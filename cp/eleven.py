a=int(input())
l=list(str(bin(a)).replace('0b',''))[::-1]

print(l)
c=0
for i in l:
    if i=='1':
        c+=1
        break
    else:
        c+=1
print(c)