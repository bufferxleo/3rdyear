from sklearn.datasets import load_iris
iris=load_iris()

x=iris.data
y=iris.target

# print(x,iris.target_names)

l=[]

for i in y:
    if i==0:
        l.append('setosa')
    elif i==1:
        l.append('versicolor')
    else:
        l.append('virginica')

y=l

# print(x,y)

import pandas as pd

df=pd.DataFrame(x)
df['target']=y

# print(df)


from sklearn.preprocessing import LabelEncoder

enc=LabelEncoder()

df['target']=enc.fit_transform(df['target'])

# print(df)


from sklearn.model_selection import train_test_split

X,x,Y,y=train_test_split(df.drop(['target'],axis=1),df.target,test_size=0.3)

df=pd.DataFrame(X)
df['target']=Y
print(df)

df=pd.DataFrame(x)
df['target']=y
print(df)