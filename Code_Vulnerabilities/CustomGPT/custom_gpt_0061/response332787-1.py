
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

# Custom cross-validation class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(0, 2, size=9)  # Binary target variable

# Define your own train-test indices
train_indices = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 8]]
test_indices = [[8], [4, 5, 6, 7]]

# Create custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Set parameters for GridSearchCV
params = {'some_param': [0.1, 1, 10]}  # Example parameter

# Create and fit the GridSearchCV
clf = GridSearchCV(estimator=SomeSklearnModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Get best parameters
print(clf.best_params_)
