from sklearn.datasets import load_iris
iris=load_iris()

x=iris.data
y=iris.target


print(x,y,x.shape,y.shape)