
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Generate sample data (substitute with your datasets)
X1, y1 = make_classification(n_samples=1000, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=1000, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=1000, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)  # Enable probability for VotingClassifier
clf3 = DecisionTreeClassifier(random_state=3)

# Fit classifiers on respective training data
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create voting classifier
voting_classifier = VotingClassifier(estimators=[
    ('rf', clf1), ('svc', clf2), ('dt', clf3)],
    voting='soft'  # Use soft voting
)

# Fit the ensemble model (you can fit it with any of the datasets)
voting_classifier.fit(X1_train, y1_train)

# Make predictions
predictions = voting_classifier.predict(X1_test)

# Evaluate model (example using accuracy)
accuracy = np.mean(predictions == y1_test)
print(f'Accuracy: {accuracy:.2f}')
