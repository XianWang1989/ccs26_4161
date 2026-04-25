
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
train_indices = [[0, 1, 2, 3, 4, 5, 6, 7], [8]]  # Adjust to zero-indexed
test_indices = [[8], [0, 1, 2, 3, 4, 5, 6, 7]]

custom_cv = CustomCV(train_indices, test_indices)

# Example of fitting GridSearchCV
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
clf = GridSearchCV(RandomForestClassifier(), param_grid={'n_estimators': [10, 20]}, cv=custom_cv)

clf.fit(X, y)
print(clf.best_params_)
