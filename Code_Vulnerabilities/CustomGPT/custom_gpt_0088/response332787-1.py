
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Create example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Custom CV class
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Initialize custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define hyperparameter grid
param_grid = {'max_depth': [2, 3, 4]}

# Initialize the classifier
clf = DecisionTreeClassifier()

# Set up GridSearchCV with custom CV
grid_search = GridSearchCV(clf, param_grid, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Display best parameters
print("Best parameters:", grid_search.best_params_)
