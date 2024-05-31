import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv('/content/Churn_Modelling.csv',index_col="RowNumber")

df

df.drop(['CustomerId','Surname'],axis=1)

geo_dummies=pd.get_dummies(df.Geography)

gender_dummies=pd.get_dummies(df.Gender)

dummies1=pd.concat([geo_dummies,gender_dummies],axis=1)

dummies1

df1=df.drop(['Geography','Gender'],axis=1)

df1

df2=df1.drop(['CustomerId',	'Surname'],axis=1)

df2

final_df1=pd.concat([df2,dummies1],axis=1)

final_df1

sns.countplot(data=final_df1,x='Exited')

final_df1.hist(figsize=(15,12),bins=15)
plt.title("Features distribution")
plt.show()

plt.figure(figsize=(15,15))
p=sns.heatmap(final_df1.corr(),annot=True)

x=final_df1.drop(['Exited'],axis=1)

x

y=final_df1.Exited

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=31)

#scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)


from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()

classifier.add(
    Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=13))

classifier.add(
    Dense(units=6,kernel_initializer='uniform',activation='relu'))

classifier.add(
    Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics='accuracy')


classifier.fit(x_train,y_train,batch_size=10,epochs=10,verbose=0)





score,acc=classifier.evaluate(x_train,y_train,batch_size=10)

print('Train_score:',score)
print('Test score:',acc)

y_pred=classifier.predict(x_test)

y_pred=(y_pred>0.5)

