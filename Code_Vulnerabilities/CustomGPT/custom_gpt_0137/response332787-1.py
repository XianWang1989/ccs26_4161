
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
            yield np.array(train_idx), np.array(test_idx)

# Sample data generation
X = np.arange(9).reshape(-1, 1)  # 9 samples, single feature
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Binary targets

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Instantiate your custom CV class
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define parameter grid for GridSearchCV
params = {'alpha': [0.1, 1, 10]}  # Example hyperparameter

# Use GridSearchCV with the custom cross-validator
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Now clf can be used to evaluate the best parameters and performance
