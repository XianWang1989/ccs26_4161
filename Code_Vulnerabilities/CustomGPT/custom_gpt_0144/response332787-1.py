from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import numpy as np

# Example data (9 samples)
X = np.random.rand(9, 2)
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Define custom train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Combine indices into a list of tuples
custom_cv = [(train, test) for train, test in zip(train_indices, test_indices)]

# Example classifier and parameter grid
clf = SVC()
param_grid = {'C': [0.1, 1, 10]}

# Use GridSearchCV with custom CV
grid_search = GridSearchCV(clf, param_grid, cv=custom_cv)
grid_search.fit(X, y)

print("Best parameters found:", grid_search.best_params_)
