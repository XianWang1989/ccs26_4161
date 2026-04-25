
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample datasets
X1, y1 = ...  # Load your first dataset
X2, y2 = ...  # Load your second dataset
X3, y3 = ...  # Load your third dataset

# Combine datasets
X = np.vstack((X1, X2, X3))
y = np.concatenate((y1, y2, y3))

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define classifiers
classifier1 = SVC(probability=True)
classifier2 = RandomForestClassifier()
classifier3 = LogisticRegression()

# Create an ensemble model
ensemble_model = VotingClassifier(estimators=[
    ('svc', classifier1),
    ('rf', classifier2),
    ('lr', classifier3)
], voting='soft')

# Fit the ensemble model
ensemble_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = ensemble_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Ensemble Model Accuracy: {accuracy:.2f}')
