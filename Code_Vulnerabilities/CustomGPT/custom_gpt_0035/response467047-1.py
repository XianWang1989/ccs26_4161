
from sklearn.ensemble import VotingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Load example datasets (replace these with your actual datasets)
data1 = load_iris()
data2 = load_iris()
data3 = load_iris()

X1, y1 = data1.data, data1.target
X2, y2 = data2.data, data2.target
X3, y3 = data3.data, data3.target

# Split into train and test sets (for demonstration)
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Train classifiers on each dataset
clf1 = DecisionTreeClassifier()
clf2 = LogisticRegression(max_iter=200)
clf3 = SVC(probability=True)

clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create an ensemble classifier
voting_clf = VotingClassifier(estimators=[
    ('dt', clf1), 
    ('lr', clf2), 
    ('svc', clf3)
], voting='soft')

# Fit the ensemble model (you can use any dataset here)
voting_clf.fit(X_train1, y_train1)  # You can choose any train data

# Make predictions
predictions = voting_clf.predict(X_test1)  # Or any test data

# Print predictions
print(predictions)
