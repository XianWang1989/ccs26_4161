
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Let's create three different datasets
X1, y1 = make_classification(n_samples=100, n_features=10, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=10, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=10, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=0)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=0)

# Define individual classifiers for each dataset
clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier()
clf3 = LogisticRegression()

# Create a StackingClassifier
stacking_clf = StackingClassifier(
    estimators=[('dt', clf1), ('rf', clf2), ('lr', clf3)],
    final_estimator=LogisticRegression()
)

# Train each classifier on its respective dataset
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Stack their predictions
X_stacked = np.column_stack((
    clf1.predict(X1_test),
    clf2.predict(X2_test),
    clf3.predict(X3_test)
))

# Train the meta-classifier
stacking_clf.fit(X_stacked, y1_test)  # Assuming the same labels for all datasets

# Make final predictions
final_predictions = stacking_clf.predict(X_stacked)

print("Final predictions:", final_predictions)
