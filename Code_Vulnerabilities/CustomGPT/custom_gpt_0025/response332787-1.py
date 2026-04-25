
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example data
X = np.arange(9).reshape(-1, 1)  # Sample features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample labels

# Define custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define a simple model and parameters for grid search
from sklearn.ensemble import RandomForestClassifier

params = {'n_estimators': [10, 20]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters:", clf.best_params_)
