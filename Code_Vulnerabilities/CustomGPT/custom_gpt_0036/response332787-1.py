
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

# Create a synthetic dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=0)

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Initialize your custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'n_estimators': [10, 20], 'max_depth': [None, 10, 20]}

# Initialize the classifier
clf = RandomForestClassifier()

# Setup GridSearchCV with your custom cross-validator
grid_search = GridSearchCV(clf, params, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Print best parameters from grid search
print("Best parameters found: ", grid_search.best_params_)
