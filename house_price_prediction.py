import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import neighbors
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from math import sqrt

df = pd.read_excel("housing.csv")

df.drop(['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus'],axis = 1, inplace=True)

categorial_cols = ['price','area','bedrooms','bathrooms','stories','parking']
df.dtypes

train,test = train_test_split(df, test_size =0.3)
x_train = train.drop('price',axis = 1)
y_train = train['price']

x_test = test.drop('price',axis = 1)
y_test = test['price']

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))

x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)

x_test_scaled = scaler.fit_transform(x_test)
x_test = pd.DataFrame(x_test_scaled)

rmse_val = []

from sklearn.neighbors import KNeighborsRegressor
model =KNeighborsRegressor(n_neighbors = 5)
model.fit(x_train, y_train) #fit the moodel
pred = model.predict(x_test) #make prediction on test set
error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
rmse_val.append(error) #store rmse values
print('RMSE value for k= ',5,'is: ',error)

fig= plt.figure()
plt.scatter(y_test,pred)
plt.title('Actual versus prediction')
plt.xlabel('Actual',fontsize=20)
plt.ylabel('predicted',fontsize=20)
