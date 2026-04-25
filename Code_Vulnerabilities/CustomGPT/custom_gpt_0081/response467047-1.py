
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Create synthetic datasets (you can replace these with your actual datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=3)

# Split the datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Train different classifiers on each dataset
clf1 = RandomForestClassifier(random_state=1)
clf1.fit(X1_train, y1_train)

clf2 = GradientBoostingClassifier(random_state=2)
clf2.fit(X2_train, y2_train)

# Here, you can add your third classifier, e.g., SVC or any custom one:
clf3 = RandomForestClassifier(random_state=3)
clf3.fit(X3_train, y3_train)

# Use VotingClassifier to ensemble the models
voting_clf = VotingClassifier(estimators=[
    ('rf1', clf1),
    ('gb', clf2),
    ('rf2', clf3)
], voting='hard')  # You can also use 'soft' for probability-based voting

# Train the ensemble model on your training sets (you could concatenate the datasets if needed)
combined_X_train = np.vstack((X1_train, X2_train, X3_train))
combined_y_train = np.hstack((y1_train, y2_train, y3_train))

voting_clf.fit(combined_X_train, combined_y_train)

# Make predictions
combined_X_test = np.vstack((X1_test, X2_test, X3_test))
combined_y_test = np.hstack((y1_test, y2_test, y3_test))

y_pred = voting_clf.predict(combined_X_test)

# Evaluate the model
accuracy = accuracy_score(combined_y_test, y_pred)
print(f'Ensemble model accuracy: {accuracy:.2f}')
