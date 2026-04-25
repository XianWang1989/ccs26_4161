
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Example datasets creation (replace this with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train models on each dataset
model1 = RandomForestClassifier()
model1.fit(X1, y1)

model2 = LogisticRegression()
model2.fit(X2, y2)

model3 = SVC(probability=True)  # Set probability=True for soft voting
model3.fit(X3, y3)

# Create a voting classifier
voting_classifier = VotingClassifier(
    estimators=[
        ('rf', model1),
        ('lr', model2),
        ('svc', model3)
    ],
    voting='soft'  # Use 'soft' for probability-based voting
)

# Combine datasets for final training
X_combined = np.vstack((X1, X2, X3))
y_combined = np.concatenate((y1, y2, y3))

# Train the ensemble model
voting_classifier.fit(X_combined, y_combined)

# Make predictions on new data
# Replace `X_new` with your new dataset
# X_new = ... (new dataset you want to predict on)
# predictions = voting_classifier.predict(X_new)
