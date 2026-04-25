
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)  # Number of folds

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example usage:
X = np.arange(1, 10).reshape(-1, 1)  # Sample feature data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample target labels

# Define your train and test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create the custom cross validator
custom_cv = CustomCV(train_indices, test_indices)

# Define the parameters for your model
params = {'some_param': [1, 2]}  # Example parameters

# Use GridSearchCV with the custom cross validator
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Access the results
print(clf.best_params_)
