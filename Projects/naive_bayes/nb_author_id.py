   #!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
#Importing GaussianNB
from sklearn.naive_bayes import GaussianNB
#for calculating accuracy
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#For Calculating Time
t0 = time()

#Making classifier
clf = GaussianNB()

#training classifier
clf.fit(features_train, labels_train)

#Time in training
print("training time:",round(time()-t0))

t0 = time()
#Calculating Prediction
pred = clf.predict(features_test)

print("Prediction time:",round(time()-t0))

#Calculating Accuracy
accuracy = accuracy_score(pred, labels_test)
print(accuracy)

#########################################################


