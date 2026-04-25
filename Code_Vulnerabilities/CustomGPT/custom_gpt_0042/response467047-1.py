
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Define individual classifiers
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)
clf3 = LogisticRegression(random_state=3)

# Fit each classifier on its respective dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Prepare predictions for each dataset
pred1 = clf1.predict(X1_test)
pred2 = clf2.predict(X2_test)
pred3 = clf3.predict(X3_test)

# Combine predictions using VotingClassifier
voter = VotingClassifier(estimators=[
    ('rf', clf1),
    ('svc', clf2),
    ('lr', clf3)],
    voting='soft')  # 'soft' uses predicted probabilities for voting

# Fit the voting classifier by stacking the input data
# Here we concatenate predictions on the test set
X_meta = np.column_stack((pred1, pred2, pred3))

# Use the labels from any dataset for fitting the voter, assuming they're the same
voter.fit(X_meta, y1_test)  # Using y1_test as labels

# Make final predictions
final_pred = voter.predict(X_meta)

# Evaluate the accuracy
accuracy = np.mean(final_pred == y1_test)
print(f"Ensemble model accuracy: {accuracy:.2f}")
