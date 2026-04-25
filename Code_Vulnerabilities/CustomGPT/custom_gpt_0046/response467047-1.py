
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and test sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define individual classifiers
classifier1 = RandomForestClassifier(random_state=42)
classifier2 = GradientBoostingClassifier(random_state=42)
classifier3 = LogisticRegression(max_iter=1000)

# Create a stacking classifier
stacking_classifier = StackingClassifier(
    estimators=[
        ('rf', classifier1),
        ('gb', classifier2),
        ('lr', classifier3)
    ],
    final_estimator=LogisticRegression()
)

# Train the stacking classifier on the combined training sets
X_train_combined = np.vstack((X1_train, X2_train, X3_train))
y_train_combined = np.concatenate((y1_train, y2_train, y3_train))

stacking_classifier.fit(X_train_combined, y_train_combined)

# Make predictions on the combined test sets
X_test_combined = np.vstack((X1_test, X2_test, X3_test))
y_test_combined = np.concatenate((y1_test, y2_test, y3_test))

predictions = stacking_classifier.predict(X_test_combined)

# Evaluate the model (you can use any metric you like)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test_combined, predictions)
print(f'Ensemble model accuracy: {accuracy:.2f}')
