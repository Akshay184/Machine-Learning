#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

# importing k-nearest neighbour
from sklearn.neighbors import KNeighborsClassifier

# importing accuracy_score from sklearn
from sklearn.metrics import accuracy_score

# importing time
from time import time


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# initilizing the timt
t0 = time()

# creating k-nearest-neighbour classifier
clf = KNeighborsClassifier(weights="distance",n_neighbors=1)

# training the classifier
clf.fit(features_train, labels_train)

# time in training the classifier
print("Training time is:",round(time()-t0),"s")

# initilizing time
t0 = time()

# predicting the ouput 
pred = clf.predict(features_test)

#time taken by classisier for the prediction
print("Prediction time is:",round(time()-t0),"s") 


# calculating the accuracy
accuracy = accuracy_score(pred, labels_test)

# printing the accuracy
print("Accuracy is:",accuracy)


#########################################################


