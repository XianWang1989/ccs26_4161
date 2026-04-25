
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create some example datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Create classifiers for each dataset
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)  # SVC requires probability=True for soft voting
clf3 = LogisticRegression()

# Train models on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier with the trained models
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')  # 'soft' voting uses predicted probabilities

# Fit the VotingClassifier on one of the datasets (you can choose based on your preference)
voting_clf.fit(X1_train, y1_train)

# Make predictions
predictions = voting_clf.predict(X1_test)
print("Predictions:", predictions)
