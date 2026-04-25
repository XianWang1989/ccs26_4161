
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Train-test split
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train your classifiers
model1 = RandomForestClassifier()
model2 = SVC(probability=True)
model3 = LogisticRegression()

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create a Voting Classifier
ensemble_model = VotingClassifier(estimators=[
    ('rf', model1),
    ('svc', model2),
    ('lr', model3)],
    voting='soft'  # 'soft' uses predicted probabilities
)

# Fit the ensemble model on the combined dataset
X_combined = np.concatenate((X1_train, X2_train, X3_train))
y_combined = np.concatenate((y1_train, y2_train, y3_train))
ensemble_model.fit(X_combined, y_combined)

# Make predictions
predictions = ensemble_model.predict(X_combined)
