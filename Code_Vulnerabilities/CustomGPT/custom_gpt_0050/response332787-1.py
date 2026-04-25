
import numpy as np
from sklearn.model_selection import GridSearchCV

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.arange(9).reshape(-1, 1)  # 9 samples
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Dummy target variable

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create an instance of your custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define your hyperparameter grid
params = {'param_name': [0.1, 1.0, 10.0]}  # Example parameter

# Use GridSearchCV with your custom CV
clf = GridSearchCV(estimator=SomeEstimator(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Now clf will use the specified splits during cross-validation
