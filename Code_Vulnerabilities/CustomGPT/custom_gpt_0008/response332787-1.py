
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Create a sample dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train-test indices
# -1 means the sample is part of the test set
# 0 means the sample is part of the train set
train_indices = [1, 3, 5, 7, 8]  # First fold training
test_indices = [0, 2, 4, 6]       # First fold testing
folds = np.array([-1] * 9)        # All samples initially marked as test
folds[train_indices] = 0           # Mark training indices

# Create PredefinedSplit
custom_cv = PredefinedSplit(test_fold=folds)

# Define the model and parameters for GridSearch
clf = RandomForestClassifier(random_state=42)
param_grid = {'n_estimators': [10, 50, 100]}

# Initialize GridSearchCV with custom cross-validation
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Output the best parameters
print("Best parameters found: ", grid_search.best_params_)
