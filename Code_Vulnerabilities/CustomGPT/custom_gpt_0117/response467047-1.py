
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Step 1: Create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Step 2: Split data into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Step 3: Train different classifiers for each dataset
model1 = RandomForestClassifier()
model1.fit(X_train1, y_train1)

model2 = SVC(probability=True)  # Set probability=True for soft voting
model2.fit(X_train2, y_train2)

model3 = LogisticRegression()
model3.fit(X_train3, y_train3)

# Step 4: Create the Voting Classifier
voting_model = VotingClassifier(estimators=[
    ('rf', model1),
    ('svc', model2),
    ('lr', model3)
], voting='soft')  # 'soft' voting considers predicted probabilities

# Step 5: Train the Voting Classifier on the combined training data
X_train_combined = np.vstack((X_train1, X_train2, X_train3))
y_train_combined = np.concatenate((y_train1, y_train2, y_train3))
voting_model.fit(X_train_combined, y_train_combined)

# Step 6: Evaluate on the combined test data
X_test_combined = np.vstack((X_test1, X_test2, X_test3))
y_test_combined = np.concatenate((y_test1, y_test2, y_test3))
accuracy = voting_model.score(X_test_combined, y_test_combined)

print(f"Ensemble Model Accuracy: {accuracy:.2f}")
