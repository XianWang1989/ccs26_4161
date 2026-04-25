
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Create synthetic datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split your datasets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
classifier1 = RandomForestClassifier(random_state=42)
classifier2 = SVC(probability=True, random_state=42)
classifier3 = LogisticRegression(random_state=42)

# Train classifiers on their respective datasets
classifier1.fit(X_train1, y_train1)
classifier2.fit(X_train2, y_train2)
classifier3.fit(X_train3, y_train3)

# Create an ensemble using VotingClassifier
voting_classifier = VotingClassifier(
    estimators=[
        ('rf', classifier1),
        ('svc', classifier2),
        ('lr', classifier3)],
    voting='soft'  # 'hard' for majority voting
)

# Optionally train on a combined dataset
# For this example, let's just fit on the test set of the first dataset
voting_classifier.fit(X_test1, y_test1)

# Make predictions
predictions = voting_classifier.predict(X_test1)

# Display predictions
print(predictions)
