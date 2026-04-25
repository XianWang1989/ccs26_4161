
import numpy as np
from sklearn.model_selection import GridSearchCV

class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield train_idx, test_idx

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example data and parameters
X = np.random.rand(9, 2)  # 9 samples, 2 features
y = np.random.randint(0, 2, size=9)  # Binary targets

# Define train-test indices
train_indices = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
test_indices = [[5, 6, 7, 8], [0, 1, 2, 3, 4]]

# Create custom CV
custom_cv = CustomCV(train_indices, test_indices)

# Example parameters for GridSearchCV
params = {'some_hyperparameter': [1, 10, 100]}

# Initialize GridSearchCV with your custom CV
clf = GridSearchCV(estimator='your_model_here', param_grid=params, cv=custom_cv)

# Fit the model (replace 'your_model_here' with an actual model, like RandomForestClassifier)
# clf.fit(X, y)
