
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])  # Sample data
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1])  # Sample target
params = {'some_parameter': [1, 2]}  # Define your parameters

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
custom_cv = CustomCV(train_indices, test_indices)

clf = GridSearchCV(estimator='your_estimator_here', param_grid=params, cv=custom_cv)
clf.fit(X, y)
