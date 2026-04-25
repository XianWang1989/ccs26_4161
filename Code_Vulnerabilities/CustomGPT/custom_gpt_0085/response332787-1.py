
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

# Sample data
X = np.arange(9).reshape(-1, 1)  # Features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Labels

# Define your custom train and test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define your model and parameter grid
params = {'some_param': [0, 1]}  # Example parameters for your estimator

# Use GridSearchCV with your custom cross-validator
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
