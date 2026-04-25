
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

# Sample data
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Custom train-test indices for 2-fold CV
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define parameter grid for GridSearchCV
param_grid = {'max_depth': [1, 2, 3]}

# Example classifier (replace with your model)
from sklearn.tree import DecisionTreeClassifier
clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output best parameters found
print("Best parameters:", clf.best_params_)
