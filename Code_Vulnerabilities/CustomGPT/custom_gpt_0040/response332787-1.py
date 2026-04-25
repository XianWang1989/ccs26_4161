
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

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
y = np.random.randint(0, 2, size=9)  # Binary target

# Define your train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of your custom cross-validation
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for GridSearchCV
params = {'some_param': [0.1, 0.2]}

# Create a GridSearchCV object with your custom cross-validation
clf = GridSearchCV(estimator=YourModel(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)
