import numpy as np

data=np.random.randint(0,100,size=(5,5))
print(data)

data=data+10

sum=np.sum(data)
mean=np.mean(data)
max=np.max(data)
min=np.min(data)

print(sum,mean,max,min)


# analysis

nonzero=np.count_nonzero(data)
print(nonzero)