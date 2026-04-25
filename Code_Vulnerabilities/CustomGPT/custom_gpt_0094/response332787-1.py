
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.arange(9).reshape(-1, 1)  # 9 samples with 1 feature
y = np.random.rand(9)  # Random target variable

# Custom indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Initialize custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for grid search
param_grid = {'alpha': [0.1, 1.0, 10.0]}

# Create GridSearchCV with custom CV
clf = GridSearchCV(estimator=YourEstimator(), param_grid=param_grid, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output best parameters
print("Best parameters found: ", clf.best_params_)
