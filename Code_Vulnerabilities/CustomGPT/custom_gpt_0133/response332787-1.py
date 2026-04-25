
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# Sample data
X = np.random.rand(9, 10)  # 9 samples, 10 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Custom indices for 2-fold cross-validation
train_indices = [[0, 1, 3, 4, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7, 8]]
test_indices = [[2], [1]]

# Custom CV class
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Set up a GridSearchCV
params = {'max_depth': [1, 2, 3]}
clf = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output results
print("Best parameters found: ", clf.best_params_)
