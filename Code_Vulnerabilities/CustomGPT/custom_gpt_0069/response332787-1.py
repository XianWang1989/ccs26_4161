
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, is_classifier
import numpy as np

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.arange(9).reshape(-1, 1)  # Sample data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample labels

train_indices = [[0, 1, 2, 3], [4, 5, 6, 7]]
test_indices = [[4, 5, 6, 7], [0, 1, 2, 3]]

# Instantiate your custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for GridSearchCV
params = {'model__parameter': [1, 2, 3]}  # Replace 'model' with your actual model name

# Assume you have a model defined, e.g., from sklearn
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

clf = GridSearchCV(model, params, cv=custom_cv)
clf.fit(X, y)

print(f'Best parameters: {clf.best_params_}')
