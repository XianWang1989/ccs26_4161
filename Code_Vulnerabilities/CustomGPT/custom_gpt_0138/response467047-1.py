
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Dummy data creation
data1 = pd.DataFrame(np.random.rand(100, 10))  # Dataset 1
data2 = pd.DataFrame(np.random.rand(100, 10))  # Dataset 2
data3 = pd.DataFrame(np.random.rand(100, 10))  # Dataset 3
labels = np.random.randint(0, 2, 100)  # Binary labels for all datasets

# Split data into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(data1, labels, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(data2, labels, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(data3, labels, test_size=0.2, random_state=42)

# Create classifiers
clf1 = RandomForestClassifier()
clf2 = LogisticRegression()
clf3 = SVC(probability=True)

# Fit the classifiers
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Prepare the ensemble classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('lr', clf2),
    ('svc', clf3)
], voting='soft')  # Use 'soft' voting for probability-based predictions

# Fit the ensemble model
voting_clf.fit(np.vstack((X_train1, X_train2, X_train3)),
                np.concatenate((y_train1, y_train2, y_train3)))

# Make predictions
predictions = voting_clf.predict(np.vstack((X_test1, X_test2, X_test3)))

# Evaluate performance
accuracy = accuracy_score(np.concatenate((y_test1, y_test2, y_test3)), predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
