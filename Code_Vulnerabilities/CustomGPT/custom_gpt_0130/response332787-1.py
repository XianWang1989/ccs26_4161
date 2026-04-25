
import numpy as np
from sklearn.model_selection import GridSearchCV

# Custom CV class
class CustomCV:
    def __init__(self, train_indices, test_indices):
        self.train_indices = train_indices
        self.test_indices = test_indices

    def split(self, X, y=None, groups=None):
        for train_idx, test_idx in zip(self.train_indices, self.test_indices):
            yield np.array(train_idx), np.array(test_idx)

    def get_n_splits(self, X=None, y=None, groups=None):
        return len(self.train_indices)

# Example usage
X = np.arange(9).reshape(-1, 1)  # Dummy feature data
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])  # Dummy target data

# Define your custom indices
train_indices = [[1, 3, 5, 7], [0, 2, 4, 6, 8]]
test_indices = [[0, 2, 4, 6, 8], [1, 3, 5, 7]]

# Create an instance of CustomCV
custom_cv = CustomCV(train_indices, test_indices)

# Define your model and parameters
params = {'your_model_param': [0.1, 0.2]}  # Adjust based on your model

# Use GridSearchCV with your custom CV
clf = GridSearchCV(your_model, params, cv=custom_cv)  # Replace 'your_model' with the actual model
clf.fit(X, y)

# Results
print(clf.best_params_)
