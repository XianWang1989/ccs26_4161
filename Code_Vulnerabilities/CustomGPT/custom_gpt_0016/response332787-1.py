
import numpy as np
from sklearn.model_selection import GridSearchCV

# Custom CV class
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        # Generate training and testing indices for each fold
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example Usage
X = np.random.rand(9, 2)  # Dummy feature set with 9 samples and 2 features
y = np.random.randint(0, 2, size=9)  # Dummy binary target variable

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of the custom CV class
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'some_param': [0.1, 0.2]}

# Create the GridSearchCV instance
clf = GridSearchCV(estimator='YourEstimatorHere', param_grid=params, cv=custom_cv)

# Fit the model
# clf.fit(X, y) # Uncomment and fit your actual model here

print(f'Number of splits: {custom_cv.get_n_splits()}')
