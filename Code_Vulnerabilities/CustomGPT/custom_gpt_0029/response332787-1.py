
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.ensemble import RandomForestClassifier

# Sample data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Target variable

# Custom indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Prepare test_fold array for PredefinedSplit
test_fold = np.array([-1]*5 + [0]*4)  # First 5 are for fold 0, next 4 for fold 1

# Instantiate PredefinedSplit
custom_cv = PredefinedSplit(test_fold)

# Define model and parameters
clf = RandomForestClassifier()
param_grid = {'n_estimators': [10, 50], 'max_depth': [None, 10]}

# Instantiate GridSearchCV
grid_search = GridSearchCV(clf, param_grid, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Best estimator
print("Best parameters:", grid_search.best_params_)
