
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


# Example usage:
X = np.random.rand(9, 5)  # Dummy feature data
y = np.random.randint(0, 2, size=9)  # Dummy target variable

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create an instance of the CustomCV
custom_cv = CustomCV(train_indices=train_indices, test_indices=test_indices)

# Define your model and parameters for GridSearch
from sklearn.ensemble import RandomForestClassifier
params = {'n_estimators': [10, 20]}

# Setup GridSearchCV with the custom CV
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Output the best parameters
print("Best parameters:", clf.best_params_)
