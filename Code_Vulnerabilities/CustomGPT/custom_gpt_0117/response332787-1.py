
from sklearn.model_selection import BaseCrossValidator
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
train_indices = [[1, 3, 5, 7], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7]]

custom_cv = CustomCV(train_indices, test_indices)
