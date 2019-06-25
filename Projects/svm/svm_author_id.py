#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

# importing SVM from sklearn
from sklearn.svm import SVC

# importing accuracy from sklearn
from sklearn.metrics import accuracy_score

# importing time package
from time import time



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# reducing the size of training data to compute fastely
# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[0:int(len(labels_train)/100)]


#########################################################
### your code goes here ###

# initilizing time
t0 = time()

# creating the classifier for SVM
clf = SVC(kernel="rbf",C=10000.0,gamma='')

# training the classifier
clf.fit(features_train, labels_train)

# c
print("Training time: ",round(time()-t0))

# initilizing time for prediction
t0 = time()

# predicting the outcome of the classifier
pred = clf.predict(features_test)

# calculating the accuracy of the algorithm
accuracy = accuracy_score(pred, labels_test)

# time taken by classifier for predicting the result
print("Prediction time: ",round(time()-t0))

# printing the accuracy
print("Accuracy is: ",accuracy)

# calculating the class to which the test data correspond
sara = 0
chris = 0
for label in pred:
    if label==1:
        chris+=1
    else:
        sara+=1
print("Number of Sara's email: ",sara)
print("Number of Chris's email: ",chris)

#########################################################


