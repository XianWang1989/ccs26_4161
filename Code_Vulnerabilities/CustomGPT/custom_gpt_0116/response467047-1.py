
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train different classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)

# Fit the classifiers
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)

# Use the fitted classifiers to predict the test set
pred1 = clf1.predict(X1_test)  # Predictions from first dataset
pred2 = clf2.predict(X2_test)  # Predictions from second dataset
# For the third dataset, you can choose a different model or reuse one
pred3 = clf1.predict(X3_test)  # Using the same model for simplicity

# Create the ensemble model using the predictions
X_ensemble = np.vstack((pred1, pred2, pred3)).T  # Combine predictions
y_ensemble = np.concatenate((y1_test, y2_test, y3_test))

# Create a voting classifier
ensemble_clf = VotingClassifier(estimators=[('rf', clf1), ('gb', clf2)], voting='hard')

# Fit the ensemble model on the combined predictions
ensemble_clf.fit(X_ensemble, y_ensemble)

# Make predictions with the ensemble model
predictions = ensemble_clf.predict(X_ensemble)

# Evaluate the ensemble model
accuracy = accuracy_score(y_ensemble, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
