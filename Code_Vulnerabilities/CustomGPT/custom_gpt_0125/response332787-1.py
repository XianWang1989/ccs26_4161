
from sklearn.model_selection import GridSearchCV, PredefinedSplit
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

# Define custom train/test indices
train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

# Create a list for the fold assignments
folds = np.array([-1] * len(X))
for i, (train, test) in enumerate(zip(train_indices, test_indices)):
    for index in test:
        folds[index] = i

# Create PredefinedSplit
custom_cv = PredefinedSplit(test_fold=folds)

# Parameters for GridSearch
params = {'param_name': [value1, value2]}  # replace with your actual parameters

# Create GridSearchCV
clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)
