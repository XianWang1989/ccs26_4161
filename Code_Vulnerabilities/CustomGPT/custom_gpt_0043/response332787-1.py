
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

# Example Data
X = np.array([[i] for i in range(9)])  # 9 samples
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample targets

# Custom indices for 2-fold CV
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate your custom cross-validation iterator
custom_cv = CustomCV(train_indices, test_indices)

# Define a simple classifier and parameter grid
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
params = {'n_estimators': [50, 100], 'max_depth': [None, 10]}

# Use GridSearchCV with your custom cross-validation iterator
grid_search = GridSearchCV(clf, params, cv=custom_cv)
grid_search.fit(X, y)

print("Best parameters:", grid_search.best_params_)
