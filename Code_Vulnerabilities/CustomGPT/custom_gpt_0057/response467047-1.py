
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split for training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers on each dataset
model1 = RandomForestClassifier(random_state=1).fit(X1_train, y1_train)
model2 = SVC(probability=True, random_state=2).fit(X2_train, y2_train)
model3 = LogisticRegression(random_state=3).fit(X3_train, y3_train)

# Create an ensemble model
ensemble_model = VotingClassifier(estimators=[
    ('rf', model1), 
    ('svc', model2), 
    ('lr', model3)],
    voting='soft')

# Train the ensemble model using predictions from each individual model
# Use predictions from training sets of each model as input features
X_train_ensemble = np.array([model1.predict_proba(X1_train)[:, 1], 
                              model2.predict_proba(X2_train)[:, 1], 
                              model3.predict_proba(X3_train)[:, 1]]).T

ensemble_model.fit(X_train_ensemble, y1_train)

# Test on the combined predictions
X_test_ensemble = np.array([model1.predict_proba(X1_test)[:, 1], 
                             model2.predict_proba(X2_test)[:, 1], 
                             model3.predict_proba(X3_test)[:, 1]]).T

ensemble_predictions = ensemble_model.predict(X_test_ensemble)

# Print the predictions
print("Ensemble predictions:", ensemble_predictions)
