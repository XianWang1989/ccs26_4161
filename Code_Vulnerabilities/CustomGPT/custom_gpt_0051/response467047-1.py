
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create synthetic datasets
X1, y1 = np.random.rand(100, 10), np.random.randint(0, 2, 100)
X2, y2 = np.random.rand(100, 10), np.random.randint(0, 2, 100)
X3, y3 = np.random.rand(100, 10), np.random.randint(0, 2, 100)

# Train classifiers on each dataset
model1 = RandomForestClassifier()
model1.fit(X1, y1)

model2 = LogisticRegression()
model2.fit(X2, y2)

model3 = SVC(probability=True)
model3.fit(X3, y3)

# Combine the trained classifiers into a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', model1),
    ('lr', model2),
    ('svc', model3)
], voting='soft')  # Use 'soft' voting to consider predicted probabilities

# Create a combined dataset for evaluation
X_combined = np.mean([X1, X2, X3], axis=0)  # Combine features by averaging
y_combined = y1  # Use any of the y arrays since they have the same labels

# Train the voting classifier
voting_clf.fit(X_combined, y_combined)

# Make predictions
predictions = voting_clf.predict(X_combined)

# Evaluate accuracy
accuracy = accuracy_score(y_combined, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
