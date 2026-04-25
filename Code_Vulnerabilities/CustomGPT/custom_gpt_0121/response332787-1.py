
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

# Example usage
X = np.arange(9).reshape(-1, 1)  # dummy feature matrix
y = np.arange(9)                  # dummy target array

train_indices = [[0, 1, 3, 4, 6, 7], [2, 5, 8]]
test_indices = [[2, 5, 8], [0, 1, 3, 4, 6, 7]]
custom_cv = CustomCV(train_indices, test_indices)

params = {'some_param': [1, 2]}  # example parameters for the model
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)

clf.fit(X, y)
