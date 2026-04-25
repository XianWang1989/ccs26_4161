
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = SVC(probability=True)
clf2 = DecisionTreeClassifier()
clf3 = RandomForestClassifier()

# Fit models on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[('svc', clf1), ('dt', clf2), ('rf', clf3)], voting='soft')
voting_clf.fit(X_train1, y_train1)  # You can choose any dataset for fitting

# Evaluate on one of the test sets
y_pred = voting_clf.predict(X_test1)
print(f'Voting Classifier Accuracy: {accuracy_score(y_test1, y_pred)}')

# Alternatively, create a Stacking Classifier
stacking_clf = StackingClassifier(estimators=[('svc', clf1), ('dt', clf2), ('rf', clf3)], final_estimator=RandomForestClassifier())
stacking_clf.fit(X_train1, y_train1)

# Evaluate the Stacking Classifier
y_pred_stacking = stacking_clf.predict(X_test1)
print(f'Stacking Classifier Accuracy: {accuracy_score(y_test1, y_pred_stacking)}')
