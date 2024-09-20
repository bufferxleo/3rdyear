x=0
y=9999999
a,b=map(int,input().split())
sign=1
if a*b<0:
    sign=-1

a,b=abs(a),abs(b)
if b!=0:
    mid=0
    while a/b!= float(f"{mid:.5f}"):
        mid=(x+y)/2

        if a/b>float(f"{mid:.5f}"):
            x=mid
        elif a/b<float(f"{mid:.5f}"):
            y=mid
        else:
            print(sign*(float(f"{mid:.5f}")))
else:
    print("division by zero error")