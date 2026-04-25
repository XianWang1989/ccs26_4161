
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your custom train-test indices
train_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]
test_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]

# Create the custom cross-validation object
custom_cv = CustomCV(train_indices, test_indices)

# Define parameters for GridSearchCV
params = {'C': [0.1, 1, 10]}

# Initialize the model
clf = GridSearchCV(LogisticRegression(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Best parameters found
print("Best parameters:", clf.best_params_)
