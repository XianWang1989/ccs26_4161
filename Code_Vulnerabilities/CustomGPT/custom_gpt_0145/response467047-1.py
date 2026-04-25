
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Simulating three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Splitting into training and test sets for each dataset
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Training the classifiers on their respective datasets
clf1 = DecisionTreeClassifier(random_state=1).fit(X1_train, y1_train)
clf2 = LogisticRegression(random_state=2).fit(X2_train, y2_train)
clf3 = SVC(probability=True, random_state=3).fit(X3_train, y3_train)

# Creating the Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('lr', clf2),
    ('svc', clf3)
], voting='soft')  # using 'soft' voting to consider predicted probabilities

# Now fit the ensemble on one of the datasets, or any common dataset
X_combined = (X1, X2, X3)  # Stack your datasets appropriately considering your case
y_combined = (y1, y2, y3)  # Stack your labels accordingly

# Fitting the Voting Classifier on your chosen dataset
voting_clf.fit(X_combined[0], y_combined[0])  # Fit on one dataset for example
voting_pred = voting_clf.predict(X_combined[1])  # Predict on another dataset

# Evaluating the ensemble
accuracy = accuracy_score(y_combined[1], voting_pred)
print(f'Ensemble model accuracy: {accuracy:.2f}')
