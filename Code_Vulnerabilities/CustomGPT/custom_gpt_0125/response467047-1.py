
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load datasets (using Iris dataset as a placeholder for illustration)
data1 = load_iris()
data2 = load_iris()
data3 = load_iris()

# Split into training and test sets for each dataset
X1_train, X1_test, y1_train, y1_test = train_test_split(data1.data, data1.target, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(data2.data, data2.target, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(data3.data, data3.target, test_size=0.2, random_state=42)

# Initialize classifiers
clf1 = RandomForestClassifier()
clf2 = GradientBoostingClassifier()
clf3 = RandomForestClassifier()

# Fit classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf1', clf1), 
    ('gb', clf2), 
    ('rf2', clf3)],
    voting='hard')

# Fit the ensemble model on one of the train sets (you might choose to stack)
voting_clf.fit(X1_train, y1_train)

# Predictions
predictions = voting_clf.predict(X1_test)

# Evaluate the model
accuracy = accuracy_score(y1_test, predictions)
print(f'Ensemble model accuracy: {accuracy:.2f}')
