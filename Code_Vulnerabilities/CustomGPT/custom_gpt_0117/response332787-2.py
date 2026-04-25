
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Create sample data
X, y = make_classification(n_samples=9, n_features=10, random_state=42)

# Define model and parameters
clf = RandomForestClassifier()
param_grid = {'n_estimators': [10, 20]}

# Setup GridSearchCV with custom cross-validator
grid_search = GridSearchCV(clf, param_grid, cv=custom_cv)

# Fit the model
grid_search.fit(X, y)

# Output the best parameters
print("Best Parameters:", grid_search.best_params_)
