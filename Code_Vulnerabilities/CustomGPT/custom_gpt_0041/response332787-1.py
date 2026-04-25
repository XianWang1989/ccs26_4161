
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train, test in zip(self.train_indices, self.test_indices):
            yield train, test

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.array([[i] for i in range(9)])  # Dummy feature data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Dummy target data

# Custom indices for train-test splits
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for GridSearch
params = {'your_model_param': [value1, value2]}  # Replace with actual params

# Initialize GridSearchCV with custom CV
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)  # Replace YourModel with your estimator

# Fit the model
clf.fit(X, y)

# Access results
print(clf.best_params_)
