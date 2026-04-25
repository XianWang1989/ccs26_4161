
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Example dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train and test indices
train_indices = np.array([[1, 3, 5, 7, 8], [0, 2, 4, 6]]).T
test_indices = np.array([[0, 2, 4, 6], [1, 3, 5, 7, 8]]).T

# Create a mask indicating the test set for each fold
# -1 means training, 0 means test
test_fold = np.array([-1]*8 + [0] + [-1]*4 + [1])
test_fold = np.concatenate(test_fold).ravel()

# Set up PredefinedSplit
custom_cv = PredefinedSplit(test_fold)

# Define your model and parameters
clf = RandomForestClassifier()
param_grid = {'n_estimators': [10, 20], 'max_depth': [None, 5]}

# Set up GridSearchCV with the custom cross-validation
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=custom_cv)

# Fit the model on the dataset
grid_search.fit(X, y)

# Display the best parameters
print("Best parameters found:", grid_search.best_params_)
