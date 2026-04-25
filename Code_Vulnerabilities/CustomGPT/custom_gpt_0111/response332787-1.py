
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

# Example of usage
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Define your train and test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define your parameters for GridSearchCV
params = {'some_param': [1, 2, 3]}  # Example parameter

# Initialize GridSearchCV with the custom cross-validator
clf = GridSearchCV(estimator='YourEstimatorHere', param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
