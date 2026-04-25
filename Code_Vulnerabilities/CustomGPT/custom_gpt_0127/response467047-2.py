
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# Generate sample datasets
X1, y1 = make_regression(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_regression(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_regression(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual regressors on each dataset
reg1 = LinearRegression().fit(X_train_1, y_train_1)
reg2 = DecisionTreeRegressor().fit(X_train_2, y_train_2)
reg3 = SVR().fit(X_train_3, y_train_3)

# Ensemble the regressors
voting_reg = VotingRegressor(estimators=[('lr', reg1), ('dt', reg2), ('svr', reg3)])
voting_reg.fit(X_train_1, y_train_1)  # Again, using any dataset for fitting

# Evaluate the ensemble
score = voting_reg.score(X_test_1, y_test_1)
print(f'Ensemble R^2 score: {score:.2f}')
