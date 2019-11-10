# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names = ['core', 'cpuCoresSize', 'cpuCachSize', 'cpuBoostSpeed', 'ramType', 'ramSize', 'storageType', 'storageSize', 'batteryCapacity', 'gpuMemorySize', 'gpuBooStSpeed', 'output']
# load dataset
laptops = pd.read_csv("D:/Tech-Ring-Team/data/laptops_points.csv", header=None, names=col_names);

print(laptops.head());

feature_cols = ['core', 'cpuCoresSize', 'cpuCachSize', 'ramType', 'ramSize', 'storageType', 'storageSize', 'batteryCapacity', 'gpuMemorySize', 'gpuBooStSpeed']
X = laptops[feature_cols] # Features
y = laptops.output # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
#
# # Create Decision Tree classifer object
clf = DecisionTreeClassifier()
#
# # Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
#
# #Predict the response for test dataset
# y_pred = clf.predict(X_test)
#
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#
