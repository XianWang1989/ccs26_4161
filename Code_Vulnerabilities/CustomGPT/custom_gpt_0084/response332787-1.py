
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
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

# Example usage
X = np.random.rand(9, 2)  # Create some random data
y = np.random.randint(0, 2, size=9)  # Random binary target

train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]  # Adjusted to 0-indexing
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

custom_cv = CustomCV(train_indices, test_indices)

params = {'model__param1': [0.1, 0.5], 'model__param2': [1, 2]}  # Replace 'model' with your model's name
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)

clf.fit(X, y)
print(clf.best_params_)
