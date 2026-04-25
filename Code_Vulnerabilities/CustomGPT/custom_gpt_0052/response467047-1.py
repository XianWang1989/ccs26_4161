
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample data creation (replace these with your actual datasets)
# Assuming X1, X2, X3 are your feature sets and y is your label array
X1 = np.random.rand(100, 10)
y = np.random.randint(0, 2, size=100)

X2 = np.random.rand(100, 10)
X3 = np.random.rand(100, 10)

# Train-test split
X_train1, X_test1, y_train, y_test = train_test_split(X1, y, test_size=0.2, random_state=42)
X_train2, X_test2, _, _ = train_test_split(X2, y, test_size=0.2, random_state=42)
X_train3, X_test3, _, _ = train_test_split(X3, y, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = SVC(probability=True)
clf2 = RandomForestClassifier()
clf3 = LogisticRegression()

# Fit models on respective datasets
clf1.fit(X_train1, y_train)
clf2.fit(X_train2, y_train)
clf3.fit(X_train3, y_train)

# Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('svc', clf1), 
    ('rf', clf2), 
    ('lr', clf3)],
    voting='soft'  # or 'hard' for hard voting
)

# Fit the voting classifier (you can fit on any dataset, using the same y)
voting_clf.fit(X_train1, y_train)  # Use any of the train sets

# Predict and evaluate
y_pred = voting_clf.predict(X_test1)  # Use the corresponding test set
accuracy = accuracy_score(y_test, y_pred)

print(f'Ensemble Model Accuracy: {accuracy:.2f}')
