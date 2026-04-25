
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, LogisticRegression
from sklearn.metrics import accuracy_score

# Generating dummy datasets
X1, y1 = make_classification(n_samples=1000, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=1000, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=1000, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define classifiers for each dataset
model1 = RandomForestClassifier(random_state=42)
model2 = GradientBoostingClassifier(random_state=42)
model3 = LogisticRegression(random_state=42)

# Fit models on their respective datasets
model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('rf', model1),
    ('gb', model2),
    ('lr', model3)],
    voting='hard')  # Use 'soft' for probability-based voting

# Fit the ensemble model on all datasets' predictions
ensemble_model.fit(X1_train, y1_train)  # You can adjust this as needed

# Make predictions
predictions = ensemble_model.predict(X1_test)  # Use the corresponding test set

# Evaluate performance
accuracy = accuracy_score(y1_test, predictions)

print(f'Ensemble Model Accuracy: {accuracy:.2f}')
