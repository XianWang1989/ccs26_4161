
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import GridSearchCV

class CustomCV(BaseEstimator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.random.rand(9, 3)  # Dummy feature data for 9 samples
y = np.random.randint(0, 2, size=9)  # Dummy labels

train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

custom_cv = CustomCV(train_indices, test_indices)
params = {'some_param': [0.1, 0.2, 0.3]}

clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

print(clf.best_params_)
