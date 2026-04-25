
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
from sklearn.model_selection import KFold

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.arange(9).reshape(-1, 1)  # Sample data
y = np.random.randint(0, 2, size=9)  # Sample labels

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create the custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'some_param': [0.1, 0.2]}

# Replace with your model, e.g., a RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print best parameters
print(clf.best_params_)
