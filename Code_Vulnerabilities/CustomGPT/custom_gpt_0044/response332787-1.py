
from sklearn.model_selection import BaseCrossValidator, GridSearchCV
import numpy as np

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def get_n_splits(self):
        return len(self.train_indices)

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

# Example data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, 9)  # Binary target

# Custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate the custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define a sample model and parameters for GridSearchCV
from sklearn.ensemble import RandomForestClassifier
params = {'n_estimators': [10, 50], 'max_depth': [None, 10]}

# Use GridSearchCV with the custom CV
clf = GridSearchCV(RandomForestClassifier(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print best parameters
print(clf.best_params_)
