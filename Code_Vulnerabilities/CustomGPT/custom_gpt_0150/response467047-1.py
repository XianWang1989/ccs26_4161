
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Simulate three different datasets
X1, y1 = np.random.rand(100, 5), np.random.randint(0, 2, 100)
X2, y2 = np.random.rand(100, 5), np.random.randint(0, 2, 100)
X3, y3 = np.random.rand(100, 5), np.random.randint(0, 2, 100)

# Split datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2)

# Initialize classifiers
clf1 = DecisionTreeClassifier()
clf2 = LogisticRegression()
clf3 = SVC(probability=True)

# Train classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create an ensemble model
ensemble_model = VotingClassifier(estimators=[('dt', clf1), ('lr', clf2), ('svc', clf3)], voting='soft')

# Train ensemble model on the first dataset for example
ensemble_model.fit(X1_train, y1_train)

# Evaluate ensemble model
accuracy = ensemble_model.score(X1_test, y1_test)
print(f'Accuracy of the ensemble model: {accuracy:.2f}')
