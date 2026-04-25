
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Generate three different datasets (example)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
model1 = RandomForestClassifier(random_state=1)
model2 = GradientBoostingClassifier(random_state=2)

model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)

# Create a voting classifier
voting_classifier = VotingClassifier(
    estimators=[
        ('rf', model1),
        ('gb', model2)
    ],
    voting='soft'  # Use 'soft' for probability based voting
)

# Train the voting classifier on a new dataset or combine predictions
# Here, we use more data for simplicity
X_train_combined = np.concatenate((X_train1, X_train2, X_train3))
y_train_combined = np.concatenate((y_train1, y_train2, y_train3))

voting_classifier.fit(X_train_combined, y_train_combined)

# Predict and evaluate
y_pred = voting_classifier.predict(X_test1)  # or any other test set
accuracy = accuracy_score(y_test1, y_pred)

print(f'Ensemble Model Accuracy: {accuracy:.2f}')
