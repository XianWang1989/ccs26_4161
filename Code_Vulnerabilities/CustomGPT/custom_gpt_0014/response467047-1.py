
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Initialize classifiers
clf1 = DecisionTreeClassifier()
clf2 = SVC(probability=True)
clf3 = LogisticRegression()

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1),
    ('svc', clf2),
    ('lr', clf3)],
    voting='soft'  # 'soft' uses predicted probabilities; 'hard' uses predicted classes
)

# Fit the voting classifier on the combined training sets
X_combined_train = np.concatenate((X1_train, X2_train, X3_train))
y_combined_train = np.concatenate((y1_train, y2_train, y3_train))
voting_clf.fit(X_combined_train, y_combined_train)

# Evaluate on combined test sets
X_combined_test = np.concatenate((X1_test, X2_test, X3_test))
y_combined_test = np.concatenate((y1_test, y2_test, y3_test))
accuracy = voting_clf.score(X_combined_test, y_combined_test)

print(f'Ensemble model accuracy: {accuracy:.2f}')
