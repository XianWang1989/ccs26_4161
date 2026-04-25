
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate dummy datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)

# Fit models
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)

# Collect predictions from the three models
pred1 = clf1.predict(X1_test)
pred2 = clf2.predict(X2_test)

# VotingClassifier using the trained models
voting_clf = VotingClassifier(estimators=[
    ('clf1', clf1),
    ('clf2', clf2)
], voting='hard')

# Fit the ensemble on one dataset (or you can use predictions)
voting_clf.fit(X1_train, y1_train)

# Make predictions
final_predictions = voting_clf.predict(X1_test)

# Evaluate the ensemble model
accuracy = accuracy_score(y1_test, final_predictions)
print(f"Ensemble Model Accuracy: {accuracy:.2f}")
