from flask import Flask, render_template, request
import LogisticRegressionModel
import NaiveBayesModel
import LinearSVCModel
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html",
                           LogisticRegressionModelAccuracy=LogisticRegressionModel.accuracy,
                           NaiveBayesModelAccuracy=NaiveBayesModel.accuracy,
                           LinearSVCModelAccuracy=LinearSVCModel.accuracy)


@app.route('/prediction', methods=['POST'])
def prediction():
    parameters = request.json
    if parameters['model'] == "LogisticRegression":
        return LogisticRegressionModel.predict_spam(parameters['question'])
    elif parameters['model'] == "NaiveBayes":
        return NaiveBayesModel.predict_spam(parameters['question'])
    elif parameters['model'] == "LinearSVC":
        return LinearSVCModel.predict_spam(parameters['question'])
    return "Invalid Parameters"


if __name__ == "__main__":
    app.run()
