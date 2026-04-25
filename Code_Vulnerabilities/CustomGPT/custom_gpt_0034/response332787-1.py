
from sklearn.model_selection import GridSearchCV, BaseCrossValidator
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

# Sample data
X = np.arange(9).reshape(9, 1)  # 9 samples
y = np.random.randint(0, 2, size=9)  # Binary target

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Create CustomCV object
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Parameters for GridSearchCV
params = {'your_model_param': [1, 2]}  # Replace with your model parameters

# Use GridSearchCV with custom CV
clf = GridSearchCV(estimator='YourModelHere', param_grid=params, cv=custom_cv)
clf.fit(X, y)

print(f"Best parameters found: {clf.best_params_}")
