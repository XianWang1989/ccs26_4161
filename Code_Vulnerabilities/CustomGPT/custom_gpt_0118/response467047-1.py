
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Create dummy datasets (replace these with your datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Train individual classifiers
clf1 = LogisticRegression()
clf2 = RandomForestClassifier()
clf3 = SVC(probability=True)

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier with the trained models
ensemble_model = VotingClassifier(estimators=[
    ('lr', clf1),
    ('rf', clf2),
    ('svc', clf3)
], voting='soft')  # Use 'soft' for averaging probabilities

# Fit the ensemble model (you can use combined features or predictions)
X_combined = np.concatenate((clf1.predict_proba(X1_test), 
                              clf2.predict_proba(X2_test),
                              clf3.predict_proba(X3_test)), axis=1)

# Assuming that y_test is the same across datasets
ensemble_model.fit(X_combined, np.concatenate((y1_test, y2_test, y3_test)))

# Make predictions
final_predictions = ensemble_model.predict(X_combined)

print(final_predictions)
