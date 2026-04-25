
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into train and test
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
model1 = LogisticRegression()
model1.fit(X_train1, y_train1)

model2 = DecisionTreeClassifier()
model2.fit(X_train2, y_train2)

model3 = SVC(probability=True)  # Enable probability estimation
model3.fit(X_train3, y_train3)

# Create an ensemble model
ensemble_model = VotingClassifier(estimators=[
    ('lr', model1),
    ('dt', model2),
    ('svc', model3)],
    voting='soft'  # Use soft voting for probability-based predictions
)

# Train the ensemble model
ensemble_model.fit(np.vstack((X_train1, X_train2, X_train3)), 
                   np.concatenate((y_train1, y_train2, y_train3)))

# Evaluate the ensemble model
accuracy = ensemble_model.score(np.vstack((X_test1, X_test2, X_test3)), 
                                 np.concatenate((y_test1, y_test2, y_test3)))

print(f'Ensemble Model Accuracy: {accuracy:.2f}')
