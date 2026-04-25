
from sklearn.base import BaseEstimator
from sklearn.model_selection import GridSearchCV
import numpy as np

class CustomCV(BaseEstimator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_index, test_index in zip(self.train_indices, self.test_indices):
            yield train_index, test_index

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[i] for i in range(9)])  # 9 samples
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Sample labels

    # Define your custom indices for 2-fold CV
    train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]  # Adjusted to zero-based index
    test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]  # Adjusted to zero-based index

    # Instantiate custom CV with defined splits
    custom_cv = CustomCV(train_indices, test_indices)

    # Define parameters for GridSearchCV
    params = {'your_model_param': [0.1, 0.2]}  # Example parameter

    # Use GridSearchCV with custom CV
    clf = GridSearchCV(estimator=YourEstimator(), param_grid=params, cv=custom_cv)

    # Fit the model
    clf.fit(X, y)

    # Output results
    print("Best parameters found: ", clf.best_params_)
