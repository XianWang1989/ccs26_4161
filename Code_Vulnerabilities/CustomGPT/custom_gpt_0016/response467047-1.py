
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Create synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into train and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define the base classifiers
base_classifiers = [
    ('rf', RandomForestClassifier(n_estimators=100)),
    ('svm', SVC(probability=True)),
    ('lr', LogisticRegression())
]

# Create a Stacking Classifier
stacking_classifier = StackingClassifier(
    estimators=base_classifiers,
    final_estimator=LogisticRegression()
)

# Fit ensemble model on dataset 1
stacking_classifier.fit(np.concatenate([X1_train, X2_train, X3_train]), 
                        np.concatenate([y1_train, y2_train, y3_train]))

# Make predictions
preds = stacking_classifier.predict(np.concatenate([X1_test, X2_test, X3_test]))

# Evaluate predictions
accuracy = np.mean(preds == np.concatenate([y1_test, y2_test, y3_test]))
print(f'Ensemble model accuracy: {accuracy:.2f}')
