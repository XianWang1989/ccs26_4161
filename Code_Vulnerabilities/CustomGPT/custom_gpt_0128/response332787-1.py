
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

# Custom cross-validation class
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Sample data: 9 samples
X = np.array([[i] for i in range(1, 10)])  # Your features
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Your target

# Custom train-test splits
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for GridSearchCV
params = {'param1': [0.1, 1.0], 'param2': [1, 10]}

# Use GridSearchCV with the custom CV
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)
clf.fit(X, y)

# Check the results
print(clf.best_params_)
