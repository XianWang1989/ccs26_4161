
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Create example datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Create individual models
model1 = RandomForestClassifier(random_state=1)
model2 = LogisticRegression(random_state=2)
model3 = SVC(probability=True, random_state=3)

# Fit the models
model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('rf', model1),
    ('lr', model2),
    ('svc', model3)
], voting='soft')

# Fit the ensemble model
ensemble_model.fit(np.vstack((X1_train, X2_train, X3_train)), 
                   np.hstack((y1_train, y2_train, y3_train)))

# Make predictions
predictions = ensemble_model.predict(np.vstack((X1_test, X2_test, X3_test)))
print("Ensemble predictions:", predictions)
