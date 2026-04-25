
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.datasets import make_classification
from sklearn.svm import SVC

# Create sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]  # Python zero indexing
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Custom cross-validation iterator
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Instantiate the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Set parameters for GridSearchCV
params = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
clf = GridSearchCV(SVC(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters found: ", clf.best_params_)
