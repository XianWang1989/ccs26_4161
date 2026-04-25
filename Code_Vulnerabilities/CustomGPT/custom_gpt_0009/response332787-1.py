
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
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

# Example usage:
X = np.arange(9).reshape(-1, 1)  # Sample data with 9 samples
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample target variable

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create a custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Set parameters for GridSearchCV
params = {'some_param': [1, 2]}  # Example params for your model

# Example classifier (replace with your model)
from sklearn.ensemble import RandomForestClassifier
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Now you can fit your model
clf.fit(X, y)

print(clf.best_params_)
