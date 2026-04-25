
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train-test split for each dataset
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Train individual models on each dataset
model1 = RandomForestClassifier()
model1.fit(X1_train, y1_train)

model2 = LogisticRegression()
model2.fit(X2_train, y2_train)

model3 = SVC(probability=True)  # Setting probability=True for voting
model3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(
    estimators=[('rf', model1), ('lr', model2), ('svc', model3)],
    voting='soft'  # 'soft' voting gives probabilities, 'hard' voting uses class labels
)

# You can now train the Voting Classifier on one of the datasets (or a combined dataset)
# For demonstration, let's use X1 and y1
voting_clf.fit(X1, y1)

# Make predictions on the test set of the first dataset (you could also choose another)
predictions = voting_clf.predict(X1_test)

# Calculate accuracy
accuracy = accuracy_score(y1_test, predictions)
print(f"Ensemble Model Accuracy: {accuracy:.2f}")
