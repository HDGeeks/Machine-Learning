import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
'''
On the original holdback data (the one not available to you), the setup here achieves a macro F1 score of .543
This is the baseline to beat!

This script here runs the same setup, but with random training/test splits made from the train.csv that is available to you.
The idea is that it provides an estimate F1 score that is somewhat comparable to the performance on the real holdback data.

This is achieved by running the experiment 100 times over different random splits and then reporting the average F1 score.
The average score after 100 runs is in the same region +/- .03 as the original holdback data.
'''
#test = pd.read_csv('holdback.csv',sep=",") #on the original holdback data, this setup achieves an F1 score (macro) of .543
count_vect = CountVectorizer()

runs = 0
f1_total = 0
for _ in range(100):
    train = pd.read_csv('/Users/hd/Desktop/Machine Learning/ML-Excercises/train.csv',sep=",")
    test = train.sample(frac=0.05)
    train = train.drop(test.index)

    trainLabels = np.array(train["targets"])
    testLabels = np.array(test["targets"])

    trainInputs = count_vect.fit_transform(train["samples"])
    testInputs = count_vect.transform(test["samples"])

    lr = LogisticRegression(penalty="l1", solver="saga", tol=0.01,random_state=218) # define the model
    lr.fit(trainInputs,trainLabels) # fit the model to the training data
    testPredict = lr.predict(testInputs) # use the model to make predictions

    f1_total += (f1_score(testLabels,testPredict,average='macro'))
    runs += 1

print (f"Average F1 after {runs} runs: {f1_total/runs}")