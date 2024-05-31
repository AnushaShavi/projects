from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf


(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()


#60000=no of rows/instances
#28x28 is dimension of each image or no of pixels=28x28(2D)==784(1D)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

x_train[0]

plt.imshow(x_train[0],'gray')

y_train[0]

#Scaling to improve accuracy
x_train=x_train/255
x_test=x_test/255

#flatten into 1D to pass as inputs
x_train_flatenned=x_train.reshape(len(x_train),784)
print(x_train_flatenned.shape)

x_test_flattened=x_test.reshape(len(x_test),784)
print(x_test_flattened.shape)

x_train_flatenned[0]

#Create a simple neural network with input layer with 784 neurons n output layer with 10 neurons
model=keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,),activation='sigmoid')
])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

model.fit(x_train_flatenned,y_train,epochs=5)

#Evaluating accuracy on testing dataset
model.evaluate(x_test_flattened,y_test)


plt.imshow(x_test[2])

y_pred=model.predict(x_test_flattened)
print(y_pred[2])

print(y_test[2])

#Finds max index and prints index of it
np.argmax(y_pred[2])

y_pred_labels=[np.argmax(i) for i in y_pred]
print(y_pred_labels)

#Build confusion matrix
cm=tf.math.confusion_matrix(labels=y_test,predictions=y_pred_labels)
cm

import seaborn as sns
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')


#Introduce an hidden layer
m=keras.Sequential([
    keras.layers.Dense(100,input_shape=(784,),activation='relu'),
    keras.layers.Dense(10,activation='sigmoid')
])
m.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

m.fit(x_train_flatenned,y_train,epochs=10)

#model evaluation
m.evaluate(x_test_flattened,y_test)

#Introduce an hidden layer with inside flatten function
m=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(10,activation='sigmoid')

])
m.compile(
    optimizer='rmsprop',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

m.fit(x_train,y_train,epochs=5)

m.evaluate(x_test,y_test)

