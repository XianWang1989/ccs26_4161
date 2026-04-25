
from sklearn.model_selection import GridSearchCV
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.random.rand(9, 10)  # Example data with 9 samples and 10 features
y = np.random.randint(0, 2, size=9)  # Example binary target

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)

params = {'parameter_name': [value1, value2]}  # Replace with actual parameters
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)
clf.fit(X, y)
