
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Generate synthetic data (3 different datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split data into train and test sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Create individual classifiers
clf1 = RandomForestClassifier()
clf2 = LogisticRegression()
clf3 = SVC(probability=True)

# Train classifiers on respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)

# Create an ensemble classifier
ensemble_model = VotingClassifier(estimators=[
    ('rf', clf1),
    ('lr', clf2),
    ('svc', clf3)],
    voting='soft'  # 'soft' uses predicted probabilities
)

# Combine predictions
# Note: You can use any dataset for the ensemble predictions here,
# usually you would use the same test set or validation set.
X_combined = np.concatenate((X_test1, X_test2, X_test3), axis=0)
y_combined = np.concatenate((y_test1, y_test2, y_test3), axis=0)

# Fit ensemble model on all datasets
ensemble_model.fit(X_combined, y_combined)

# Make predictions
predictions = ensemble_model.predict(X_combined)

# Check accuracy
accuracy = np.mean(predictions == y_combined)
print(f'Ensemble model accuracy: {accuracy:.2f}')
