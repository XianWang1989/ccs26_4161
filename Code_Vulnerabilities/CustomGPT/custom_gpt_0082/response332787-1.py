
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X, y = make_classification(n_samples=9, n_features=5, random_state=42)

# Custom train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Initialize custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Define your model and parameters
clf = RandomForestClassifier(random_state=42)
params = {'n_estimators': [50, 100], 'max_depth': [None, 10]}

# Set up GridSearchCV
grid_search = GridSearchCV(estimator=clf, param_grid=params, cv=custom_cv)

# Fit model
grid_search.fit(X, y)

# Output best parameters
print("Best parameters found: ", grid_search.best_params_)
