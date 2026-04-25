
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin, is_classifier
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield np.array(train), np.array(test)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example Data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Create train and test indices
train_indices = [[0, 1, 3, 4, 5], [2, 6, 7, 8]]
test_indices = [[2, 6, 7, 8], [0, 1, 3, 4, 5]]

# Custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Model and GridSearch
clf = GridSearchCV(LogisticRegression(), param_grid={'C': [0.1, 1, 10]}, cv=custom_cv)
clf.fit(X, y)

# Best parameters
print("Best Parameters:", clf.best_params_)
