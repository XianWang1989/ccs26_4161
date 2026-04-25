
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
import numpy as np

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
X = np.arange(9).reshape(-1, 1)  # Example data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Example target

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]  # 1st and 2nd folds
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for a GridSearchCV
params = {'n_neighbors': [1, 2, 3]}

from sklearn.neighbors import KNeighborsClassifier

clf = GridSearchCV(KNeighborsClassifier(), params, cv=custom_cv)
clf.fit(X, y)

# Best parameters
print(clf.best_params_)
