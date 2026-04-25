
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train different classifiers on each dataset
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
model3 = SVC(probability=True)  # Enable probabilities for voting

model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create a Voting Classifier
voting_clf = VotingClassifier(estimators=[
    ('logreg', model1),
    ('dt', model2),
    ('svc', model3)],
    voting='soft'  # Use 'hard' for majority voting, 'soft' for probabilities
)

# Fit on the combined training set (for demonstration)
X_combined_train = np.concatenate((X1_train, X2_train, X3_train))
y_combined_train = np.concatenate((y1_train, y2_train, y3_train))

voting_clf.fit(X_combined_train, y_combined_train)

# Make predictions
X_combined_test = np.concatenate((X1_test, X2_test, X3_test))
y_combined_test = np.concatenate((y1_test, y2_test, y3_test))

y_pred = voting_clf.predict(X_combined_test)

# Evaluate the model
accuracy = accuracy_score(y_combined_test, y_pred)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
