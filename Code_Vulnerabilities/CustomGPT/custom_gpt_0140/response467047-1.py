
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Sample datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train classifiers on individual datasets
clf1 = RandomForestClassifier()
clf1.fit(X1, y1)

clf2 = SVC(probability=True)  # SVC requires probability=True for voting
clf2.fit(X2, y2)

clf3 = LogisticRegression()
clf3.fit(X3, y3)

# Create an ensemble model using VotingClassifier
voting_clf = VotingClassifier(
    estimators=[
        ('rf', clf1),
        ('svc', clf2),
        ('lr', clf3)
    ],
    voting='soft'  # Use 'hard' for majority voting, 'soft' for probability weighted
)

# You can now evaluate your ensemble model
# Note: Make sure to stack the predictions correctly if needed
X_combined = X1  # Replace with appropriate data for evaluation
y_combined = y1  # Replace with appropriate labels for evaluation

# Evaluate the ensemble model
scores = cross_val_score(voting_clf, X_combined, y_combined, cv=5)
print(f'Ensemble model accuracy: {scores.mean():.2f} ± {scores.std():.2f}')
