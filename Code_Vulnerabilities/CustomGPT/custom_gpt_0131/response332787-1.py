
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

# Example usage
X = np.arange(9).reshape(-1, 1)  # Dummy data with 9 samples
y = np.random.randint(0, 2, size=9)  # Dummy target variable

train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

custom_cv = CustomCV(train_indices, test_indices)

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

params = {'n_estimators': [50, 100], 'max_depth': [None, 10, 20]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters found: ", clf.best_params_)
