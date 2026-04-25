
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, is_classifier
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])  # Replace with your actual features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Replace with your actual target

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Instantiate custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for GridSearchCV
params = {'your_param': [value1, value2]}  # Replace with your actual hyperparameters

# Creating the classifier (replace with your actual model)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

# Using GridSearchCV with custom cross-validator
grid_search = GridSearchCV(estimator=clf, param_grid=params, cv=custom_cv)
grid_search.fit(X, y)

# Results
print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validated score: ", grid_search.best_score_)
