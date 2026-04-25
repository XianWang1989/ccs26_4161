
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Create a sample dataset
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your own train-test indices
train_indices = np.array([[1, 3, 5, 7, 8], [0, 2, 4, 6]])
test_indices = np.array([[0, 2, 4, 6], [1, 3, 5, 7, 8]])

# Create an array that specifies which fold each sample belongs to
# -1 for training indices, corresponding to the fold it belongs to.
test_fold = np.array([-1] * X.shape[0])
for i in range(len(train_indices)):
    for index in test_indices[i]:
        test_fold[index] = i

# Instantiate PredefinedSplit with the test fold array
custom_cv = PredefinedSplit(test_fold)

# Setup parameter grid for GridSearchCV
params = {'n_estimators': [10, 20], 'max_depth': [None, 10, 20]}

# Initialize the classifier
clf = RandomForestClassifier()

# Create and fit GridSearchCV with the custom cross-validation
grid_search = GridSearchCV(clf, params, cv=custom_cv)
grid_search.fit(X, y)

# Display best parameters
print("Best parameters found: ", grid_search.best_params_)
