
import numpy as np
from sklearn.model_selection import GridSearchCV, BaseCrossValidator

class CustomCV(BaseCrossValidator):
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.random.rand(9, 2)  # 9 samples, 2 features
    y = np.random.randint(0, 2, size=9)  # Binary target

    # Custom indices
    train_indices = [[1, 3, 5, 7, 8], [0, 2, 4, 6]]
    test_indices = [[0, 2, 4, 6], [1, 3, 5, 7, 8]]

    # Create custom CV
    custom_cv = CustomCV(train_indices, test_indices)

    # Define parameters for GridSearchCV
    params = {'some_param': [1, 2, 3]}  # Replace with your actual parameters

    # Initialize GridSearchCV with custom CV
    clf = GridSearchCV(estimator='your_estimator', param_grid=params, cv=custom_cv)

    # Fit the model (replace 'your_estimator' with an actual estimator)
    # clf.fit(X, y)

