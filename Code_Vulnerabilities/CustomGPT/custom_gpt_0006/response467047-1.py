
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create example datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
model1 = DecisionTreeClassifier()
model1.fit(X1_train, y1_train)

model2 = SVC(probability=True)
model2.fit(X2_train, y2_train)

model3 = LogisticRegression()
model3.fit(X3_train, y3_train)

# Create an ensemble using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('dt', model1),
    ('svc', model2),
    ('lr', model3)],
    voting='soft'  # Use 'soft' for probability-based voting
)

# Train ensemble model on the combined dataset
ensemble_model.fit(X1_train, y1_train)  # Fit on any of the training sets

# Make predictions and evaluate
predictions = ensemble_model.predict(X1_test)  # Use any test set
accuracy = accuracy_score(y1_test, predictions)

print(f'Ensemble model accuracy: {accuracy:.2f}')
