
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create sample datasets (for demonstration purposes)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split each dataset into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Create and train classifiers for each dataset
clf1 = LogisticRegression()
clf1.fit(X1_train, y1_train)

clf2 = DecisionTreeClassifier()
clf2.fit(X2_train, y2_train)

clf3 = SVC(probability=True)  # Setting probability=True for soft voting
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('dt', clf2), ('svc', clf3)],
    voting='soft'  # Use 'hard' for majority voting
)

# Fit the VotingClassifier (you can use one of the datasets, here we use X1)
voting_clf.fit(X1_train, y1_train)

# Make predictions and evaluate
y_pred = voting_clf.predict(X1_test)
print(f'Ensemble Model Accuracy: {accuracy_score(y1_test, y_pred):.2f}')
