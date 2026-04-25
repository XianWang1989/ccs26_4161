
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, LogisticRegression, SVC, VotingClassifier
from sklearn.metrics import accuracy_score

# 1. Create synthetic datasets (you would replace this with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# 2. Split datasets into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# 3. Train different classifiers
clf1 = RandomForestClassifier()
clf1.fit(X_train1, y_train1)

clf2 = LogisticRegression()
clf2.fit(X_train2, y_train2)

clf3 = SVC(probability=True) # SVC needs to have probability=True for voting
clf3.fit(X_train3, y_train3)

# 4. Create a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('lr', clf2), 
    ('svc', clf3)
], voting='soft') # 'soft' voting uses predicted probabilities 

# 5. Train the voting classifier on one of the datasets' training set
voting_clf.fit(X_train1, y_train1) # You can choose one of the trained sets

# 6. Evaluate the ensemble model
y_pred = voting_clf.predict(X_test1) # Predict on the corresponding test set
accuracy = accuracy_score(y_test1, y_pred)
print(f'Ensemble Accuracy: {accuracy:.2f}')
