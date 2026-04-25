
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Example data
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Define your own splits
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create the custom CV iterator
custom_cv = CustomCV(train_indices, test_indices)

# Specify the parameters for GridSearchCV
params = {'n_estimators': [10, 20], 'max_depth': [None, 10, 20]}
clf = GridSearchCV(RandomForestClassifier(), params, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print the best parameters found by GridSearchCV
print("Best parameters:", clf.best_params_)
