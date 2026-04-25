
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

    # Define your train-test indices
    train_indices = [[1, 3, 5, 7, 9], [2, 4, 6, 8]]
    test_indices = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

    # Create the custom cross-validator
    custom_cv = CustomCV(train_indices, test_indices)

    # Define parameters for GridSearchCV
    params = {'n_neighbors': [1, 3, 5]}

    # Initialize GridSearchCV with custom CV
    clf = GridSearchCV(estimator='YourEstimatorHere', param_grid=params, cv=custom_cv)

    # Fit the model (assuming 'YourEstimatorHere' is replaced with an actual estimator)
    # clf.fit(X, y)
