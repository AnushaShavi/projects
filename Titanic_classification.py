# **K-Nearest Neighbor classification with Titanic dataset**

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler  #feature Scaling
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,confusion_matrix

#load the dataset
df=pd.read_csv('Titanic_dataset.csv')
df.head()


df.head()

df.describe()

df.info()

df.dtypes

df.shape

df.columns

#let 1:survived,0:not survived
x=df.drop('Survived',axis=1)    #features
y=df['Survived']
x          #labels


#Split the dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=34)


#feature scaling
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

#Initialise the KNN model
knn_model=KNeighborsClassifier(n_neighbors=5)

#Train the model
knn_model.fit(x_train_scaled,y_train)


#Predictions on training dataset
y_pred=knn_model.predict(x_test_scaled)


y_pred

# **Calculations of Performance Metrics**

from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,confusion_matrix
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
conf_matrix=confusion_matrix(y_test,y_pred)

#print metrics
print("Accuracy:::",accuracy)
print("Precision:::",precision)
print("Recall:", recall)
print("F1-Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

#Confusion matrix
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

subset_features=['Pclass',	'Sex',	'Age',	'Fare']

conf_matrix=confusion_matrix(y_test,y_pred)

plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True,  cmap='Blues', xticklabels=['Not Survived', 'Survived'],
            yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion matrix')
plt.show()


# ***Visualising the Titanic Dataset***

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('titanic.csv')
df

subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']


#create pairplot for selected features
sns.pairplot(df[subset_features],hue='Survived')
plt.show()

#visualise survival by class and sex using barplots
plt.figure(figsize=(10,10))
sns.countplot(data=df,x='Pclass',hue='Survived')
plt.title('Survival by class')
plt.show()

#countplot for sex
plt.figure(figsize=(10,10))
sns.countplot(data=df,x='Sex',hue='Survived')
plt.title('Survival by Sex')
plt.show()

#Visualise age distribution by class and survival
plt.figure(figsize=(10,10))
sns.boxplot(data=df,x='Pclass',y='Age',hue='Survived')
plt.title('Age distribution by class and survival')
plt.show()

#Visualise Fare distribution by class and survival
plt.figure(figsize=(10,10))
sns.boxplot(data=df,x='Pclass',y='Fare',hue='Survived')
plt.title('Fare distribution by class and survival')
plt.show()

#Heatmap to visualise correlations among numerical features
corr_matrix=df[subset_features].corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


import seaborn as sns
#subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']
sns.violinplot(data=df, x='Survived', y='Pclass', hue='Sex')
plt.title('Violin plot of Pclass')
plt.show()

import seaborn as sns
#subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']
sns.violinplot(data=df, x='Survived', y='Sex', hue='Sex')
plt.title('Violin plot of Sex')
plt.show()

import seaborn as sns
#subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']
sns.violinplot(data=df, x='Survived', y='Age', hue='Sex')
plt.title('Violin plot of Age')
plt.show()

import seaborn as sns
#subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']
sns.violinplot(data=df, x='Survived', y='Fare', hue='Sex')
plt.title('Violin plot of Fare')
plt.show()

import seaborn as sns
#subset_features=['Survived','Pclass',	'Sex',	'Age',	'Fare',	'Embarked']
sns.violinplot(data=df, x='Survived', y='Embarked', hue='Sex')
plt.title('Violin plot of Embarked')
plt.show()

