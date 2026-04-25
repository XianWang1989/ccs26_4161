
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

# Example training and test indices
train_indices = [[0, 1, 2, 3, 4, 5], [6, 7, 8]]
test_indices = [[6, 7, 8], [0, 1, 2, 3, 4, 5]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Sample data
X = np.random.rand(9, 3)  # 9 samples with 3 features
y = np.random.randint(0, 2, 9)  # Binary target

# Parameters for GridSearchCV
params = {'parameter_name': [0.1, 0.2, 0.3]}  # Replace with actual parameter names

# Create and fit GridSearchCV
clf = GridSearchCV(estimator='your_estimator_here', param_grid=params, cv=custom_cv)
clf.fit(X, y)
