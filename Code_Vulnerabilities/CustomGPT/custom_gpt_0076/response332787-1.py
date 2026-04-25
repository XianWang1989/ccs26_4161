
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        # Ensure indices are valid
        if len(self.train_indices) != len(self.test_indices):
            raise ValueError("Train and test indices must have the same length.")
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Define custom train-test indices
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Create custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for grid search
params = {'some_param': [1, 2, 3]}  # Adjust to your model's parameters

# Create GridSearchCV object
clf = GridSearchCV(estimator='your_model',  # Replace with your model
                   param_grid=params,
                   cv=custom_cv)

# Fit the model
clf.fit(X, y)
