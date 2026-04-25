
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(0, 2, size=9)  # Binary target (0 or 1)

# Custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Instantiate the custom CV class
custom_cv = CustomCV(train_indices, test_indices)

# Parameters for GridSearchCV
params = {"some_param": [1, 2, 3]}  # Replace with actual model parameters

# Example model (replace with your specific model)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

# Using GridSearchCV with the custom CV
grid_search = GridSearchCV(clf, params, cv=custom_cv)
grid_search.fit(X, y)

# Print results
print("Best Parameters:", grid_search.best_params_)
