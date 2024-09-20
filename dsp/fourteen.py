from sklearn.datasets import load_iris
iris=load_iris()
import pandas as pd
import seaborn as sns

x=iris.data
y=iris.target

df=pd.DataFrame(x)
df.columns=iris.feature_names
df['species']=y

sns.kdeplot((df['sepal length (cm)'],df['sepal width (cm)']))