
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
import numpy as np

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
X = np.arange(9).reshape(-1, 1)  # 9 samples, 1 feature
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Binary target

# Custom train-test indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

custom_cv = CustomCV(train_indices, test_indices)

# Define your parameters for GridSearchCV
params = {'some_param': [1, 2, 3]}  # Replace with actual parameter names

# Set up the GridSearchCV
clf = GridSearchCV(estimator='your_model', param_grid=params, cv=custom_cv)  # Replace 'your_model' with your actual model

# Fit the GridSearchCV
clf.fit(X, y)

# Access results
print(clf.best_params_)
