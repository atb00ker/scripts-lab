import pandas as pd
import numpy as np
import pickle
# scikit-learn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score

# DataSet
data_set = pd.read_csv('SpamCollection', delimiter='\t', header=None)
x_train_data, x_test_data, y_train, y_test = train_test_split(
    data_set[1], data_set[0], test_size=0.15)

# Vectorizers
vectorizer = CountVectorizer()

# Naive Bayes
x_train = vectorizer.fit_transform(x_train_data)
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

# Testing Accuracy
x_test = vectorizer.transform(x_test_data)
predictions = classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print('Accuracy score: {}'.format(accuracy))


def predict_spam(input):
    x_test = vectorizer.transform([input])
    prediction = classifier.predict(x_test)
    return prediction[0]
