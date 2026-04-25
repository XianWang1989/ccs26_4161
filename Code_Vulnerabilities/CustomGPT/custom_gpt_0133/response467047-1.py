
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Create and train classifiers
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = RandomForestClassifier()

clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Use the trained classifiers to make predictions
pred1 = clf1.predict(X_test1)
pred2 = clf2.predict(X_test2)
pred3 = clf3.predict(X_test3)

# Combine predictions with VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('lr', clf1), 
    ('dt', clf2), 
    ('rf', clf3)], 
    voting='hard'  # or use 'soft' for probability-based voting
)

# Fit the voting classifier on one of the datasets (or a combined dataset)
voting_clf.fit(X1, y1)

# Evaluate the model
final_predictions = voting_clf.predict(X_test1)  # or any test dataset you prefer
print(final_predictions)
