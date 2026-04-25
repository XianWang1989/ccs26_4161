
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def _iterTestIndices(self):
        for test_idx in self.test_indices:
            yield test_idx

# Example usage
X = np.arange(9).reshape((9, 1))  # Sample data, 9 samples
y = np.random.rand(9)  # Sample target

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
custom_cv = CustomCV(train_indices, test_indices)

params = {'some_param': [1, 2, 3]}  # Example parameter grid
clf = GridSearchCV(estimator='DummyClassifier', param_grid=params, cv=custom_cv)

# Fit the model (using a dummy classifier here for example)
clf.fit(X, y)
