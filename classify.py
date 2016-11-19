#!/usr/bin/env python3
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn import cross_validation
import numpy as np

from sklearn.externals import joblib

# load the mnist dataset
mnist_dataset = datasets.load_digits()

# split into test and train and cv
X_train, X_test, y_train, y_test = model_selection.train_test_split(mnist_dataset.data, mnist_dataset.target, test_size=0.8)

# fit a logistic regression model to the data 
model = LogisticRegression()
train_size, train_scores, test_scores = model_selection.learning_curve(model, X_train, y_train, train_sizes=np.linspace(.1,1.0,5))
model.fit(X_train, y_train)

print(model)
print((train_scores, train_size, test_scores))
joblib.dump(model, 'model.pkl')

# make predictions
expected = y_test
predicted = model.predict(X_test)
# print (expected) #Actual Digits 
# print (predicted) #Model prediction 

print ("Accuracy: ", metrics.accuracy_score(y_test, predicted)*100, "%")

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print (metrics.confusion_matrix(y_test, predicted))

#cross-validation
scores = cross_validation.cross_val_score(LogisticRegression(), mnist_dataset.data, mnist_dataset.target, scoring='accuracy', cv=10)

print (scores[1]) # Do something with the cross validation scores pls!

#TODO - Percision, Recall , F1, F2 score
