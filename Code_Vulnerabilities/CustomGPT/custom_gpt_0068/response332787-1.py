
import numpy as np
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.svm import SVC

# Let's create some sample data
X = np.random.rand(9, 5)  # 9 samples, 5 features
y = np.random.randint(0, 2, size=9)  # Binary target

# Define your own train-test indices
# For the 2-fold CV, you can set up the test indices as follows:
# - First fold: Test on samples 2, 4, 6, 8
# - Second fold: Test on samples 1, 3, 5, 7, 9
# We specify which training/testing fold each sample belongs to
test_fold = np.array([-1, 0, 0, 0, 1, 1, 1, 1, 1])  # -1 means training, 0 and 1 denote test folds

# Create a PredefinedSplit CV object
custom_cv = PredefinedSplit(test_fold)

# Set up your grid search
params = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
clf = GridSearchCV(SVC(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print the best parameters
print("Best parameters found: ", clf.best_params_)
