
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create synthetic datasets (replace with your actual data)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into training and testing sets for each dataset
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=0)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=0)

# Train individual classifiers on each dataset
model1 = RandomForestClassifier(random_state=1)
model1.fit(X1_train, y1_train)

model2 = LogisticRegression(max_iter=1000, random_state=2)
model2.fit(X2_train, y2_train)

model3 = SVC(probability=True, random_state=3)
model3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', model1),
    ('lr', model2),
    ('svc', model3)
], voting='soft')  # Use 'soft' for probability-based voting

# Fit the voting classifier on one of the datasets (or a combined dataset if applicable)
voting_clf.fit(X1_train, y1_train)  # Here, using the first dataset for simplicity

# Predict and evaluate
y_pred = voting_clf.predict(X1_test)
accuracy = accuracy_score(y1_test, y_pred)

print(f'Ensemble model accuracy: {accuracy:.2f}')
