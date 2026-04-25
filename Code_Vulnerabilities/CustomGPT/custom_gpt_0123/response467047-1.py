
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = RandomForestClassifier()
clf2 = SVC(probability=True)
clf3 = LogisticRegression()

# Fit the classifiers
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)
], voting='soft')  # 'soft' uses predicted probabilities

# Train the voting classifier
voting_clf.fit(X1_train, y1_train)  # You can use any dataset for fitting

# Make predictions
predictions = voting_clf.predict(X1_test)

# Evaluate the model (you can use accuracy, precision, etc.)
from sklearn.metrics import accuracy_score
print('Ensemble Model Accuracy:', accuracy_score(y1_test, predictions))
