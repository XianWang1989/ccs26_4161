
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = SVC(probability=True)

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('logistic', model1),
    ('tree', model2),
    ('svc', model3)
], voting='soft')  # Use 'soft' for probability-based voting

# Fit the ensemble model
ensemble_model.fit(np.vstack((X1_train, X2_train, X3_train)), np.concatenate((y1_train, y2_train, y3_train)))

# Evaluate the ensemble model
ensemble_accuracy = ensemble_model.score(np.vstack((X1_test, X2_test, X3_test)), np.concatenate((y1_test, y2_test, y3_test)))

print(f'Ensemble Model Accuracy: {ensemble_accuracy:.2f}')
