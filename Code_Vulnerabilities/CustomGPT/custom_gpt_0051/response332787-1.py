
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

# Example usage
X = np.random.rand(9, 5)  # Example feature data with 9 samples and 5 features
y = np.random.randint(0, 2, size=9)  # Example target data

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create custom CV object
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'param1': [1, 2], 'param2': [0.1, 0.2]}  # Example parameters for a model

# Initialize GridSearchCV with custom CV
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
