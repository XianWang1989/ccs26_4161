
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
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
# Sample data
X = np.random.rand(9, 10)  # 9 samples, 10 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Custom indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'some_parameter': [0.1, 1.0, 10.0]}

# Initialize GridSearchCV
clf = GridSearchCV(estimator='SomeEstimator', param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
