
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

# Example data
X = np.arange(9).reshape(-1, 1)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom CV object
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Parameters for GridSearchCV
params = {'some_param': [0, 1]}  # Update with actual parameters for your model
clf = GridSearchCV(estimator='YourEstimatorHere', param_grid=params, cv=custom_cv)

# Fit model (replace 'YourEstimatorHere' with an actual estimator)
# clf.fit(X, y)
