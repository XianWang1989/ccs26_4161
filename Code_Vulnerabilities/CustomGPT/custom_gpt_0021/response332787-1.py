
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, 9)  # Binary target

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create a custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Set up the GridSearchCV
params = {'some_param': [1, 2, 3]}  # Replace with your actual parameters
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

print("Best parameters found: ", clf.best_params_)
