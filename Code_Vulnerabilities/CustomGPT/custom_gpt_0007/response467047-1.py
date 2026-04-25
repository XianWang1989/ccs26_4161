
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Assuming we have three different datasets and classifiers
# Here we generate three synthetic datasets for demonstration purposes
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split datasets into train and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=1)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=1)

# Initialize classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = GradientBoostingClassifier(random_state=2)

# Train the classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)

# For the third dataset, let's say we're using the same classifier
# Alternatively, you can use another classifier here
clf3 = RandomForestClassifier(random_state=3)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('gb', clf2),
    ('rf3', clf3)
], voting='hard')  # Use 'soft' for probability-based voting

# Train the VotingClassifier on the first dataset
voting_clf.fit(X1_train, y1_train)

# Make predictions using the VotingClassifier on the test set of the first dataset
y_pred = voting_clf.predict(X1_test)

# Calculate accuracy
accuracy = accuracy_score(y1_test, y_pred)
print(f'Accuracy of Voting Classifier: {accuracy:.2f}')
