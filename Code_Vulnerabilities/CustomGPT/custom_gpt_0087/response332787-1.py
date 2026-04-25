
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def _iter_test_indices(self):
        return self.test_indices

# Example data
X = np.random.rand(9, 3)  # 9 samples, 3 features
y = np.random.randint(0, 2, size=9)  # Binary target variable

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Hyperparameters for GridSearchCV
params = {'some_parameter': [1, 2, 3]}  # Example parameter

# Assume clf is your classifier, e.g. RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters:", clf.best_params_)
