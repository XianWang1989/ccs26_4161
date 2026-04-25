
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate sample data for three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)

clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)

# Assuming clf3 is fitted with dataset 3
clf3 = RandomForestClassifier(random_state=3)  # Change according to the classifier you want
clf3.fit(X3_train, y3_train)

# Create an ensemble model
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('gb', clf2),
    ('rf3', clf3)  # Adjust this if clf3 is different
], voting='hard')

# Fit the ensemble on combined training sets
voting_clf.fit(X1_train, y1_train)  # Repeat for other datasets or use a combined dataset

# Evaluate the ensemble
y_pred = voting_clf.predict(X1_test)
print(f'Ensemble Accuracy: {accuracy_score(y1_test, y_pred)}')
