
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

# Custom cross-validator
class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data and parameters
X = np.random.rand(9, 10)  # Example feature data with 9 samples, 10 features
y = np.random.randint(0, 2, size=9)  # Example binary target variable
params = {'n_estimators': [10, 50, 100]}  # Example parameters for grid search

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Initialize custom cross-validator
custom_cv = CustomCV(train_indices, test_indices)

# Initialize GridSearchCV with the custom cross-validator
clf = GridSearchCV(estimator=my_model, param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Now, clf contains the results of the grid search with your custom CV splits
