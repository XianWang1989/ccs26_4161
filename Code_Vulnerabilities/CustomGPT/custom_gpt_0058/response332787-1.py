
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Create sample data
X, y = make_classification(n_samples=9, n_features=5)

# Define your own train-test indices
train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

# Instantiate your custom cross-validation iterator
custom_cv = CustomCV(train_indices, test_indices)

# Set up the model and parameters
clf = GridSearchCV(RandomForestClassifier(), param_grid={'n_estimators': [10, 20]}, cv=custom_cv)

# Fit the model
clf.fit(X, y)

# Print the best parameters found
print(clf.best_params_)
