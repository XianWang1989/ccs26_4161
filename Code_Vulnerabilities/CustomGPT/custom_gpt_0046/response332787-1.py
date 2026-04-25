
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def _iter_test_indices(self):
        return iter(self.test_indices)

# Example usage with dummy data
X = np.random.rand(9, 3)  # 9 samples, 3 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Define your model and parameters for Grid Search
from sklearn.ensemble import RandomForestClassifier

params = {'n_estimators': [10, 20], 'max_depth': [None, 10, 20]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters found: ", clf.best_params_)
