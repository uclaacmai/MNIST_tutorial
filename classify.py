#!/usr/bin/env python3
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.externals import joblib

# load the mnist dataset
mnist_dataset = datasets.load_digits()

# split into test and train and cv
X_train, X_test, y_train, y_test = cross_validation.train_test_split(mnist_dataset.data, mnist_dataset.target, test_size=0.5)

# fit a logistic regression model to the data 
model = LogisticRegression()
model.fit(X_train, y_train)
print(model)
joblib.dump(model, 'model.pkl')

# make predictions
expected = y_test
predicted = model.predict(X_test)
# print (expected) #Actual Digits 
# print (predicted) #Model prediction 

print ("Accuracy: ", metrics.accuracy_score(y_test, predicted)*100, "%")

# summarize the fit of the model

#TODO - Percision, Recall , F1, F2 score
print(metrics.classification_report(expected, predicted))
