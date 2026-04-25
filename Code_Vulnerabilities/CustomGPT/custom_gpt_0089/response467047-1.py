
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Example data preparation
# Assuming X1, X2, X3 are your three different datasets
# Y is the common label array for the datasets
X1, X2, X3 = np.random.rand(100, 10), np.random.rand(100, 10), np.random.rand(100, 10)  # Replace with your data
Y = np.random.randint(0, 2, size=100)  # Replace with your labels

# Split each dataset into training and testing sets
X1_train, X1_test, Y_train, Y_test = train_test_split(X1, Y, test_size=0.2, random_state=42)
X2_train, X2_test, _, _ = train_test_split(X2, Y, test_size=0.2, random_state=42)
X3_train, X3_test, _, _ = train_test_split(X3, Y, test_size=0.2, random_state=42)

# Train individual classifiers on each dataset
model1 = RandomForestClassifier(random_state=42)
model2 = LogisticRegression()
model3 = SVC(probability=True)

model1.fit(X1_train, Y_train)
model2.fit(X2_train, Y_train)
model3.fit(X3_train, Y_train)

# Create an ensemble voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', model1),
    ('lr', model2),
    ('svc', model3)
], voting='soft')  # Use 'soft' for weighted probabilities

# Fit the ensemble model (you can use any of the datasets)
voting_clf.fit(X1_train, Y_train)

# Make predictions
predictions = voting_clf.predict(X1_test)

# Evaluate the ensemble model
accuracy = accuracy_score(Y_test, predictions)
print(f'Ensemble model accuracy: {accuracy:.2f}')
