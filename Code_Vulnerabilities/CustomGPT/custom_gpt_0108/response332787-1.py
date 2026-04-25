
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example data
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [0, 1, 0, 1, 0, 1, 0, 1, 0]

# Define your train/test indices
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Create your custom cross-validation object
custom_cv = CustomCV(train_indices, test_indices)

# Set up your GridSearchCV
params = {'param_name': [value1, value2]}  # Replace with your parameters
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)

# Fit your model
clf.fit(X, y)
