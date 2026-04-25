
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

# Example data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, size=9)  # Binary target variable

# Define your custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Create custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Example parameter grid for GridSearchCV
params = {'model_param': [0.1, 0.2, 0.3]}  # Example parameter

# Initialize GridSearchCV with custom cross-validator
clf = GridSearchCV(estimator='your_model', param_grid=params, cv=custom_cv)

# Fit the model (replace 'your_model' with the actual model)
# clf.fit(X, y)  # Uncomment this line when you replace 'your_model'
