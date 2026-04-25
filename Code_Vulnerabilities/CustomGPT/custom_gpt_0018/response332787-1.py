
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Creating a sample dataset with 9 samples
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your custom train-test split indices
train_indices = np.array([[1, 3, 5, 7, 8], [0, 2, 4, 6]]).flatten()
test_indices = np.array([[0, 2, 4, 6], [1, 3, 5, 7, 8]]).flatten()

# Create a test fold array
test_fold = np.zeros(X.shape[0])
test_fold[train_indices] = -1  # Train samples
test_fold[test_indices] = [0, 1]  # Test fold labels

# Creating the PredefinedSplit object
custom_cv = PredefinedSplit(test_fold)

# Setting up the GridSearchCV
params = {'n_estimators': [10, 50, 100]}
clf = GridSearchCV(RandomForestClassifier(), param_grid=params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Check the best parameters
print("Best parameters found:", clf.best_params_)
