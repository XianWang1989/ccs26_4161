
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import BaseCrossValidator
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
X = np.arange(9).reshape(-1, 1)  # Sample data with 9 samples
y = np.random.randint(0, 2, size=9)  # Sample binary target variable
params = {'some_param': [1, 2, 3]}  # Example hyperparameters

# Define your custom training and test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Create an instance of the CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Initialize GridSearchCV with the custom cross-validator
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)

# Fit the model (replace 'your_model_here' with your actual model)
# clf.fit(X, y)
