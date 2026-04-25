
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import is_classifier
from sklearn.model_selection import BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data preparation
X = np.random.rand(9, 2)  # 9 samples with 2 features
y = np.random.randint(0, 2, size=9)  # Binary target variable

# Custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Create the custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'your_model_param': [0.1, 0.2]}  # Replace with your actual model parameters

# Create the GridSearchCV with the custom cross-validator
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

print("Best parameters:", clf.best_params_)
