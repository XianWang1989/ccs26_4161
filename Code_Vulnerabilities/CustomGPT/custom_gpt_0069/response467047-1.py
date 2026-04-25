
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generating three different datasets
X1, y1 = make_classification(n_samples=1000, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=1000, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=1000, n_features=20, random_state=3)

# Splitting datasets into train and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train classifiers for each dataset
clf1 = RandomForestClassifier(random_state=1).fit(X1_train, y1_train)
clf2 = SVC(probability=True, random_state=2).fit(X2_train, y2_train)
clf3 = LogisticRegression(random_state=3).fit(X3_train, y3_train)

# Create a voting classifier
voting_clf = VotingClassifier(
    estimators=[('rf', clf1), ('svc', clf2), ('lr', clf3)],
    voting='soft'  # Use 'soft' voting for probabilities
)

# Fit the voting classifier using any of the datasets (here we use the first)
voting_clf.fit(X1_train, y1_train)

# Predict on the test set
predictions = voting_clf.predict(X1_test)

# Evaluate the model
accuracy = voting_clf.score(X1_test, y1_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
