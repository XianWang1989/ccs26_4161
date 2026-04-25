
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted

# Define your custom CV class
class CustomCV(BaseEstimator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Define your custom indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create the custom CV object
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Set up the GridSearchCV
clf = GridSearchCV(estimator='your_model', param_grid={'some_param': [1, 2, 3]}, cv=custom_cv)

# Fit the model
clf.fit(X, y)
