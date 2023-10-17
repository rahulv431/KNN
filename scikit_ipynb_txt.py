# -*- coding: utf-8 -*-
"""scikit.ipynb.txt

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tu6K07eqOu42LAMqKb6YVOrEbTA2Vnqz

<a href="https://colab.research.google.com/github/Navan0/tot/blob/master/scikit.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

from IPython.display import IFrame
IFrame('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', width=10, height=20)

"""- 150 **observations**
- 4 **features** (sepal length, sepal width, petal length, petal width)
- **Response** variable is the iris species
- **Classification** problem since response is categorical
- More information in the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris)

# Training a machine learning model with scikit-learn

## Agenda

- What is the **K-nearest neighbors** classification model?
- What are the four steps for **model training and prediction** in scikit-learn?
- How can I apply this pattern to **other machine learning models**?

## K-nearest neighbors (KNN) classification
"""

# import load_iris function from datasets module
from sklearn.datasets import load_wine

# save "bunch" object containing iris dataset and its attributes
iris = load_wine()

# store feature matrix in "X"
X = iris.data

# store response vector in "y"
y = iris.target

# print the shapes of X and y
print(X.shape)
print(y.shape)

"""## scikit-learn 4-step modeling pattern

**Step 1:** Import the class you plan to use
"""

from sklearn.neighbors import KNeighborsClassifier

"""**Step 2:** "Instantiate" the "estimator"

- "Estimator" is scikit-learn's term for model
- "Instantiate" means "make an instance of"
"""

knn = KNeighborsClassifier(n_neighbors=1)

"""- Name of the object does not matter
- Can specify tuning parameters (aka "hyperparameters") during this step
- All parameters not specified are set to their defaults
"""

print(knn)

"""**Step 3:** Fit the model with data (aka "model training")

- Model is learning the relationship between X and y
- Occurs in-place
"""

knn.fit(X, y)

"""**Step 4:** Predict the response for a new observation

- New observations are called "out-of-sample" data
- Uses the information it learned during the model training process
"""

knn.predict([[3,5,4,2,1,7,6,8,9,6,5,4,1]])

"""- Returns a NumPy array
- Can predict for multiple observations at once
"""

X_new = [[3,5,4,2,1,7,6,8,10,9,11,14,12], [5,4,3,2,7,6,8,1,4,7,2,11,12]]
knn.predict(X_new)

"""## Using a different value for K"""

# instantiate the model (using the value K=5)
knn = KNeighborsClassifier(n_neighbors=5)

# fit the model with data
knn.fit(X, y)

# predict the response for new observations
knn.predict(X_new)

"""## Using a different classification model"""

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X, y)

# predict the response for new observations
logreg.predict(X_new)

from sklearn.datasets import load_wine
data = load_wine()
data.target[[10, 80, 140]]
array([0, 1, 2])
list(data.target_names)
['class_0', 'class_1', 'class_2']

"""## Resources

- [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html) (user guide), [KNeighborsClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) (class documentation)
- [Logistic Regression](http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) (user guide), [LogisticRegression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) (class documentation)
- [Videos from An Introduction to Statistical Learning](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/)
    - Classification Problems and K-Nearest Neighbors (Chapter 2)
    - Introduction to Classification (Chapter 4)
    - Logistic Regression and Maximum Likelihood (Chapter 4)
"""