
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate example datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define individual classifiers
classifier1 = DecisionTreeClassifier(random_state=1)
classifier2 = RandomForestClassifier(random_state=2)
classifier3 = SVC(probability=True, random_state=3)

# Train individual classifiers on their respective datasets
classifier1.fit(X1_train, y1_train)
classifier2.fit(X2_train, y2_train)
classifier3.fit(X3_train, y3_train)

# Predict on the test sets
pred1 = classifier1.predict(X1_test)
pred2 = classifier2.predict(X2_test)
pred3 = classifier3.predict(X3_test)

# Now combine the predictions using VotingClassifier
# Here, we will fit the voting classifier on the combined dataset
X_combined = np.array([pred1, pred2, pred3]).T  # Shape (n_samples, n_classifiers)
y_combined = y1_test  # Assuming similar labels across datasets

voting_classifier = VotingClassifier(estimators=[
    ('dt', classifier1), ('rf', classifier2), ('svc', classifier3)],
    voting='soft'  # 'soft' uses predicted probabilities
)

# Train the voting classifier on the combined dataset
voting_classifier.fit(X_combined, y_combined)

# Make final predictions
final_predictions = voting_classifier.predict(X_combined)

# Evaluate accuracy
accuracy = accuracy_score(y_combined, final_predictions)
print(f'Ensemble Voting Classifier Accuracy: {accuracy:.2f}')
