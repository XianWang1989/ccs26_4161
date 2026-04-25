
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
            yield np.array(train_idx), np.array(test_idx)

# Example usage
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Specify your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

custom_cv = CustomCV(train_indices, test_indices)

# Define your model parameters
params = {'C': [0.1, 1, 10]}  # Example parameter for SVC

# Create GridSearchCV with the custom CV
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
