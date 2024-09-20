from sklearn.datasets import load_iris
iris=load_iris()
import pandas as pd

x=iris.data
y=iris.target

df=pd.DataFrame(x)
df['target']=y

from sklearn.model_selection import train_test_split
X,x,Y,y=train_test_split(df.drop(['target'],axis=1),df.target,test_size=0.2)

df=pd.DataFrame(X)
df['target']=Y
print(df)

df=pd.DataFrame(x)
df['target']=y
print(df)