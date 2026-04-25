
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Create sample data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define custom train/test splits
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Flatten the lists to create a single list of indices
def create_cv_indices(train, test):
    return np.array([-1 if i in test else 0 for i in range(len(X))])

cv_indices = np.array([create_cv_indices(train, test) for train, test in zip(train_indices, test_indices)]).flatten()

# Create PredefinedSplit for cross-validation
cv = PredefinedSplit(test_fold=cv_indices)

# Define the classifier and parameter grid
clf = RandomForestClassifier()
param_grid = {'n_estimators': [10, 50], 'max_depth': [None, 10, 20]}

# Create GridSearchCV with the custom CV
grid_search = GridSearchCV(clf, param_grid, cv=cv)
grid_search.fit(X, y)

# Show the best parameters found
print("Best parameters:", grid_search.best_params_)
