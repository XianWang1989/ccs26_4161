
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import train_test_split

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.random.rand(9, 2)  # Sample data with 9 samples and 2 features
y = np.random.randint(0, 2, size=9)  # Sample targets

train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

custom_cv = CustomCV(train_indices, test_indices)

params = {'C': [0.1, 1, 10]}
clf = GridSearchCV(estimator=ClassifierMixin(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output results
print("Best parameters found: ", clf.best_params_)
