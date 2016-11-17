from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation


# load the mnist dataset
# TODO split into test and train and cv
mnist_dataset = datasets.load_digits()
# cross_validation.train_test_split(mnist_dataset, test_size=0.8)

# fit a logistic regression model to the data 
model = LogisticRegression()
model.fit(mnist_dataset.data, mnist_dataset.target)
print(model)

# make predictions
expected = mnist_dataset.target
predicted = model.predict(mnist_dataset.data)

# summarize the fit of the model

#TODO - Percision, Recall , F1, F2 score
print(metrics.classification_report(expected, predicted))
