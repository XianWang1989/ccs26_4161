
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.model_selection import KFold
import numpy as np

class CustomCV(BaseEstimator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample Data
X = np.arange(9).reshape(9, 1)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Define your train and test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create an instance of the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Sample parameters for GridSearchCV
params = {'param1': [0.1, 0.2], 'param2': [10, 20]}

# Example classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

# Create GridSearchCV with custom CV
grid_search = GridSearchCV(clf, params, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Print the results
print("Best parameters found: ", grid_search.best_params_)
