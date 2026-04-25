
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create synthetic datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual models
model1 = RandomForestClassifier(random_state=1)
model1.fit(X1_train, y1_train)

model2 = GradientBoostingClassifier(random_state=2)
model2.fit(X2_train, y2_train)

model3 = RandomForestClassifier(random_state=3)  # Assuming you could use same model type
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('rf1', model1), 
    ('gb2', model2), 
    ('rf3', model3)
], voting='hard')  # 'hard' voting for majority choice, use 'soft' for probabilities

# Train the ensemble model on combined data (you can also use individual predictions)
ensemble_model.fit(np.vstack((X1_train, X2_train, X3_train)), 
                   np.hstack((y1_train, y2_train, y3_train)))

# Evaluate the ensemble model
predictions = ensemble_model.predict(np.vstack((X1_test, X2_test, X3_test)))
accuracy = accuracy_score(np.hstack((y1_test, y2_test, y3_test)), predictions)

print(f'Ensemble model accuracy: {accuracy:.2f}')
