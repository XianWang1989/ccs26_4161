
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, LogisticRegression
from sklearn.metrics import accuracy_score

# Sample data generation (replace this with your datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Splitting data (replace with your actual datasets)
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)
clf3 = LogisticRegression(random_state=3)

# Train classifiers on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create a VotingClassifier with the trained classifiers
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('gb', clf2), 
    ('lr', clf3)],
    voting='hard'  # Use 'soft' for probability averages
)

# Combine the features for ensembling
X_combined = np.concatenate((X_test1, X_test2, X_test3), axis=0)
y_combined = np.concatenate((y_test1, y_test2, y_test3), axis=0)

# Train the VotingClassifier on the combined datasets
voting_clf.fit(X_combined, y_combined)

# Evaluate the ensemble's performance
y_pred = voting_clf.predict(X_combined)
accuracy = accuracy_score(y_combined, y_pred)

print(f'Ensemble model accuracy: {accuracy:.2f}')
