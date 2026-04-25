
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, is_classifier
import numpy as np

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
X = np.arange(9).reshape(-1, 1)  # Dummy features
y = np.random.randint(0, 2, size=9)  # Dummy binary labels

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)
clf = GridSearchCV(estimator=YourEstimator(), param_grid=your_param_grid, cv=custom_cv)

# Now fit the model
clf.fit(X, y)
