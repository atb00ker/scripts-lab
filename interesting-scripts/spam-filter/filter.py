import pandas as pd
import numpy as np
# scikit-learn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer,
    HashingVectorizer
)
from sklearn.model_selection import train_test_split, cross_val_score

# DataSet
data_set = pd.read_csv('SpamCollection', delimiter='\t', header=None)
x_train_data, x_test_data, y_train, y_test = train_test_split(
    data_set[1], data_set[0], test_size=0.15)

# Vectorizers
# vectorizer = HashingVectorizer()
vectorizer = CountVectorizer()
# vectorizer = TfidfVectorizer(min_df=1,stop_words='english')

# Logistic Regression
x_train = vectorizer.fit_transform(x_train_data)
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

# Testing Accuracy
x_test = vectorizer.transform(x_test_data)
predictions = classifier.predict(x_test)
print('Accuracy score: {}'.format(accuracy_score(y_test, predictions)))
# print('Precision score: {}'.format(precision_score(y_test, predictions, average='weighted')))
# print('Recall score: {}'.format(recall_score(y_test, predictions, average='weighted')))
# print('F1 score: {}'.format(f1_score(y_test, predictions, average='weighted')))
