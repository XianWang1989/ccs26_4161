
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator

# Custom CV Class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(2, size=9)  # Binary target

# Define custom train-test splits
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Instantiate the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Use GridSearchCV with the custom CV
params = {'some_param': [0.1, 0.2, 0.3]}  # Example parameters for a model
clf = GridSearchCV(estimator=SomeModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Output the best parameters
print("Best parameters:", clf.best_params_)
