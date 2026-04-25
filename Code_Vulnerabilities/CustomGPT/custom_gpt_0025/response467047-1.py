
# Import necessary libraries
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into training and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.3, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Train individual classifiers
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = SVC(probability=True)  # Setting probability=True for VotingClassifier

# Fit the models
model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)
model3.fit(X_train3, y_train3)

# Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('lr', model1), 
    ('dt', model2), 
    ('svc', model3)],
    voting='soft'  # Use 'soft' for probability-based voting
)

# Fit the voting classifier
voting_clf.fit(X_train1, y_train1)  # Can fit on one dataset; they share the same labels

# Evaluate the ensemble model
y_pred = voting_clf.predict(X_test1)
print("Voting Classifier Accuracy:", accuracy_score(y_test1, y_pred))

# Optionally for Stacking Classifier
stacking_clf = StackingClassifier(estimators=[
    ('lr', model1), 
    ('dt', model2), 
    ('svc', model3)],
    final_estimator=LogisticRegression()  # A final model on the top of the base models
)

# Fit the stacking classifier
stacking_clf.fit(X_train1, y_train1)

# Evaluate
y_pred_stacking = stacking_clf.predict(X_test1)
print("Stacking Classifier Accuracy:", accuracy_score(y_test1, y_pred_stacking))
