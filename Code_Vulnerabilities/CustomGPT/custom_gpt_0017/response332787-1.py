
import numpy as np
from sklearn.base import is_classifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Sample data
X = np.random.rand(9, 2)  # Example feature set with 9 samples and 2 features
y = np.random.randint(0, 2, size=9)  # Example binary target

# Custom train-test indices
train_indices = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7, 8]]
test_indices = [[8], [4]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define your model and parameters
from sklearn.ensemble import RandomForestClassifier
params = {'n_estimators': [50, 100]}

# Initialize GridSearchCV with custom cross-validator
clf = GridSearchCV(estimator=RandomForestClassifier(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# View best parameters
print("Best parameters found: ", clf.best_params_)
