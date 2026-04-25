
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Create synthetic datasets (replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define your individual classifiers
classifier1 = LogisticRegression()
classifier2 = DecisionTreeClassifier()
classifier3 = SVC(probability=True)

# Fit individual models on their respective datasets
classifier1.fit(X1_train, y1_train)
classifier2.fit(X2_train, y2_train)
classifier3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('logistic', classifier1),
    ('tree', classifier2),
    ('svc', classifier3)
], voting='soft')  # Use 'soft' voting for probability based weighting

# Fit the ensemble on one of the datasets (you can choose any)
voting_clf.fit(X1_train, y1_train)

# Make predictions on the test set of one of the datasets
predictions = voting_clf.predict(X1_test)

# Evaluate the ensemble
accuracy = np.mean(predictions == y1_test)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
