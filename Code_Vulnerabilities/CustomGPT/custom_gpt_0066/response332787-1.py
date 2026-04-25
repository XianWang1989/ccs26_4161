
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.arange(9).reshape(-1, 1)  # Dummy feature data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Dummy target data

train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

custom_cv = CustomCV(train_indices, test_indices)

# Assuming you have a classifier and parameters set up
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
params = {'n_estimators': [10, 20], 'max_depth': [None, 10]}
grid_search = GridSearchCV(clf, params, cv=custom_cv)

# Run grid search
grid_search.fit(X, y)

print(grid_search.best_params_)
