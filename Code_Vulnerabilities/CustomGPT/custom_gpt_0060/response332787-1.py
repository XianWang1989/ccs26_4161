
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X = np.random.rand(9, 3)  # 9 samples with 3 features
y = np.random.randint(0, 2, size=9)  # Binary target variable

# Custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]  # Train sets for 2 folds
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]  # Test sets for 2 folds

# Instantiate the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Model and grid parameters
clf = DecisionTreeClassifier()
param_grid = {'max_depth': [None, 1, 2, 3, 4]}

# Set up GridSearchCV
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=custom_cv, scoring='accuracy')

# Fit the grid search
grid_search.fit(X, y)

# Print the best parameters found
print("Best parameters found:", grid_search.best_params_)
print("Best cross-validated score:", grid_search.best_score_)
