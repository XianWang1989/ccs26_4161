
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier, LogisticRegression, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic data for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = LogisticRegression(random_state=1)
clf3 = GradientBoostingClassifier(random_state=1)

# Train classifiers on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Prepare test datasets for ensemble
pred1 = clf1.predict(X_test1)
pred2 = clf2.predict(X_test2)
pred3 = clf3.predict(X_test3)

# Combine predictions into a single dataset for ensemble
X_test_combined = np.array([pred1, pred2, pred3]).T

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('gb', clf3)
], voting='hard')

# Fit voting classifier
voting_clf.fit(X_test_combined, y_test1)  # You can use any target

# Make final predictions
final_predictions = voting_clf.predict(X_test_combined)

# Evaluate and print accuracy
accuracy = accuracy_score(y_test1, final_predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
