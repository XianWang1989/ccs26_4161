
import numpy as np
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create a custom split generator
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Initialize your custom cross-validation
custom_cv = CustomCV(train_indices, test_indices)

# Set parameters for GridSearchCV
params = {'your_model_param': [0.1, 0.2, 0.3]}  # example parameter for a model

# Use GridSearchCV with your custom CV
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# View the best parameters
print(clf.best_params_)
