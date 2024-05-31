import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC



i=datasets.load_iris()

print(i.feature_names)
print(i.target)

iris_petals=pd.DataFrame(i["data"][:,(2,3)],columns=('petal_length','petal_width'))
iris_petals['target']=i['target']
iris_petals

import seaborn as sns
import matplotlib.pyplot as plt

sns.FacetGrid(iris_petals, hue="target", palette="hls", height=5)\
   .map(plt.scatter, 'petal_length', 'petal_width')\
   .add_legend()

  #In the plot labels 1 and 2 are not linearly separable

x=i['data'][:,(2,3)]    #petal length and petal width
y=(i['target']==2).astype(np.float64)  #ouput as 1 if iris-virginica labelled as 2 or else output is 0
y
#here y has only iris-virginica cluster as 1 ,0 means iris-setosa and iris-versicolor clusters

#create a pipeline with standardscaler and linearSVC objects
svm_clf=Pipeline([("scaler",StandardScaler()),
                  ("linear_svc",LinearSVC(C=1,loss='hinge')),])
svm_clf.fit(x,y)

#C=1 means larger distance between 2 lines(wider path with more generisability)


print(svm_clf.predict([[5.5,1.7]]))
print(svm_clf.predict([[4.4,1.2]]))
print(svm_clf.predict([[2.1,0.4]]))


#Non linear SVC classification
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline

df=datasets.make_moons()
df
print(df[1])

x,y=datasets.make_moons(n_samples=100,noise=0.1)

plt.plot(x[:,0][y==0],x[:,1][y==0],'b.')
plt.plot(x[:,0][y==1],x[:,1][y==1],'g.')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
svm_p=Pipeline([
    ('scaler',StandardScaler()),
    ('Poly_features',PolynomialFeatures(degree=3)),
    ('svm_poly3',LinearSVC(C=10,loss='hinge'))

])
svm_p.fit(x,y)

print(svm_p.predict([[0.5,-0.6]]))

#using polynomial kernel trick
from sklearn.svm import SVC
svm_kernel=Pipeline([
    ('scaler',StandardScaler()),
    ('svm_poly_k',SVC(kernel='poly',degree=3,C=10))

])
svm_kernel.fit(x,y)

print(svm_kernel.predict([[0.5,-0.6]]))
