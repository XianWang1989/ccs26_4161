
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
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

# Your custom indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Sample data and parameter grid
X = np.random.rand(9, 5)  # 9 samples with 5 features
y = np.random.randint(0, 2, size=9)  # Binary target
params = {'model__parameter': [1, 2, 3]}  # Example parameter grid

# Initialize GridSearchCV
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)
clf.fit(X, y)
