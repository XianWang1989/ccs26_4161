
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

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
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.rand(9)      # Target variable

train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

custom_cv = CustomCV(train_indices, test_indices)
params = {'param1': [1, 2], 'param2': [3, 4]}  # Example parameters

clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

print(clf.best_params_)
