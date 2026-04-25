
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

# Example usage
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Example with GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Sample data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, size=9)  # binary target

# Define parameters for grid search
params = {'n_estimators': [10, 50], 'max_depth': [None, 10]}

# GridSearchCV with custom cross-validator
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)
clf.fit(X, y)

print("Best parameters found: ", clf.best_params_)
