
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

# Sample data
X = np.random.rand(9, 2)  # 9 samples with 2 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Custom train-test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Instantiate the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define a classifier and parameters
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

params = {'n_estimators': [10, 50], 'max_depth': [None, 5]}

# Use GridSearchCV with the custom cross-validator
grid_search = GridSearchCV(estimator=clf, param_grid=params, cv=custom_cv)
grid_search.fit(X, y)

# Results
print("Best parameters found: ", grid_search.best_params_)
