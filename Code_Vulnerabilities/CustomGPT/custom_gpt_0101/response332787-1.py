
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

# Sample dataset
X = np.random.rand(9, 5)
y = np.random.randint(0, 2, size=9)

# Define custom train-test splits
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom cross-validation instance
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'model_param': [0.1, 0.01]}

# Set up GridSearchCV
clf = GridSearchCV(estimator=SomeModel(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
