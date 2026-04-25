
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Generate sample data for three different datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
rf = RandomForestClassifier()
lr = LogisticRegression()
svc = SVC(probability=True) # SVC needs probability=True for voting

rf.fit(X_train1, y_train1)
lr.fit(X_train2, y_train2)
svc.fit(X_train3, y_train3)

# Create an ensemble of classifiers
voting_clf = VotingClassifier(estimators=[
    ('rf', rf),
    ('lr', lr),
    ('svc', svc)],
    voting='soft') # Use 'soft' if you want to use predicted probabilities.

# Fit the voting classifier
# Note: You have to stack the datasets appropriately to fit voting classifier
X_train_all = np.concatenate((X_train1, X_train2, X_train3), axis=0)
y_train_all = np.concatenate((y_train1, y_train2, y_train3), axis=0)

voting_clf.fit(X_train_all, y_train_all)

# Make final predictions
predictions = voting_clf.predict(X_test1) # You can test on any of the datasets

print("Predictions:", predictions)
