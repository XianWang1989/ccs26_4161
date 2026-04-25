
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

# Example data and indices
X = np.random.rand(9, 10)  # Example feature matrix
y = np.random.randint(0, 2, size=9)  # Example labels

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Example usage with GridSearchCV
params = {'alpha': [0.1, 0.2, 0.3]}  # Hyperparameters for the model
clf = GridSearchCV(estimator=None, param_grid=params, cv=custom_cv)
