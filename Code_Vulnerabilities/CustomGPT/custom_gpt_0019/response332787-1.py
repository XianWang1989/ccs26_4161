
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example Data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Create a custom CV instance
custom_cv = CustomCV(train_indices, test_indices)

# Parameter grid for GridSearchCV
params = {'some_parameter': [0.1, 0.2, 0.3]}  # Replace with your model's parameters

# Use GridSearchCV with the custom CV
clf = GridSearchCV(estimator='your_model_here',  # Replace with your estimator
                   param_grid=params,
                   cv=custom_cv)

# Fit the model (assuming your_model_here is a valid estimator)
# clf.fit(X, y)
