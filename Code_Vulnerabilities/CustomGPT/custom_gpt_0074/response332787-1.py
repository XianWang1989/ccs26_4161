
from sklearn.base import BaseCrossValidator
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

# Example usage
train_indices = [[0, 1, 2, 3, 4, 5, 6, 7], [8]]
test_indices = [[8], [0, 1, 2, 3, 4, 5, 6, 7]]

custom_cv = CustomCV(train_indices, test_indices)

# Sample GridSearchCV usage
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Sample data
X = np.random.rand(9, 10)  # 9 samples, 10 features
y = np.random.randint(0, 2, size=9)  # Binary target

params = {'n_estimators': [10, 20], 'max_depth': [None, 10]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

print("Best parameters found: ", clf.best_params_)
