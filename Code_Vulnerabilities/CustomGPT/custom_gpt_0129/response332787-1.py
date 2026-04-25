
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validation object
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define model and parameters for GridSearch
clf = DecisionTreeClassifier()
params = {'max_depth': [1, 2, 3]}

# Implement GridSearchCV with custom cross-validation
grid_search = GridSearchCV(clf, params, cv=custom_cv)
grid_search.fit(X, y)

# Output the best parameters
print("Best parameters found:", grid_search.best_params_)
