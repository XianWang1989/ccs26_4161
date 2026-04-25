
from sklearn.base import BaseEstimator, is_classifier
from sklearn.model_selection import GridSearchCV
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample Data
X = np.arange(9).reshape(-1, 1)  # Example feature set (9 samples)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Example target

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6, 7]]
test_indices = [[0, 2, 4, 6, 7], [1, 3, 5, 8]]

# Instantiate your custom cross-validation
custom_cv = CustomCV(train_indices, test_indices)

# Define your model and parameters for GridSearchCV
from sklearn.linear_model import LogisticRegression

params = {'C': [0.1, 1, 10]}
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit your model
clf.fit(X, y)

# Print the best parameters
print("Best parameters found: ", clf.best_params_)
