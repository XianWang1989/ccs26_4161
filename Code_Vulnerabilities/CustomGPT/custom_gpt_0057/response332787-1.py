
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Sample data creation
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Define hyperparameter grid
params = {'n_estimators': [5, 10], 'max_depth': [2, 3]}

# Perform GridSearchCV with custom cross-validation
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)
clf.fit(X, y)

# Output the best parameters
print("Best parameters found:", clf.best_params_)
