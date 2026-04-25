
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Custom cross-validation class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

# Create a sample dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Instantiate the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'n_estimators': [10, 50], 'max_depth': [None, 5, 10]}

# Create a GridSearchCV object
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Display best parameters
print("Best Parameters:", clf.best_params_)
