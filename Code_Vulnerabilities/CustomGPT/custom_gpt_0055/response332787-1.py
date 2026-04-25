
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Binary target

# Define custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create the custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Define parameter grid for GridSearchCV
params = {'param1': [0.1, 0.2], 'param2': [1, 2]}

# Initialize GridSearchCV with the custom CV
clf = GridSearchCV(estimator='YourEstimatorHere', param_grid=params, cv=custom_cv)

# Fit the model (replace 'YourEstimatorHere' with the actual estimator you want to use)
# clf.fit(X, y)
