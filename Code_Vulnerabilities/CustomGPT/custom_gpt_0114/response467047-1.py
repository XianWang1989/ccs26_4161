
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train classifiers on each dataset
clf1 = LogisticRegression().fit(X1, y1)
clf2 = SVC(probability=True).fit(X2, y2)
clf3 = RandomForestClassifier().fit(X3, y3)

# Create the ensemble classifier
voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('svc', clf2), ('rf', clf3)],
    voting='soft'  # Use 'soft' for probabilities or 'hard' for majority voting
)

# Assume you have a common test dataset to evaluate the ensemble
X_test = X1  # Using X1 as an example, adapt as needed
y_test = y1  # Using y1 as an example, adapt as needed

# Fit the ensemble classifier on one of the datasets or use a combined approach
voting_clf.fit(X1, y1)  # You can fit on any dataset

# Make predictions
predictions = voting_clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
