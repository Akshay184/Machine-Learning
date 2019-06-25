#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

# importing nearest neighbour algorithm
from sklearn.neighbors import KNeighborsClassifier

# importing accuracy_score
from sklearn.metrics import accuracy_score

# importing time
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# initilizing the current time
t0 = time()

# creating the classifier
clf = KNeighborsClassifier()

# training the classifier
clf.fit(features_train, labels_train)

# timi in training the classifier
print("Training time is:",round(time()-t0),"s")

# initilizing the current time
t0 = time()

# predicting the outpt of the classifier
pred = clf.predict(features_test)

# time in prediction
print("Prediction time:",round(time()-t0),"s")

# calculating the accuracy
accuracy = accuracy_score(pred, labels_test)

# pinting the accuracy
print("Accuracy is:",accuracy)





try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
