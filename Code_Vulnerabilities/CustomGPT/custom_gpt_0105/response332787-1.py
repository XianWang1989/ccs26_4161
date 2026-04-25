
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

# Example data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, 9)  # 9 binary target variables

# Define your train-test indices
train_indices = [[0, 1, 2, 3, 4, 5], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Create the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define your parameters and model
params = {'some_param': [1, 2, 3]}  # Example parameter grid
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
