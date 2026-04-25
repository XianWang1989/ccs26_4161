
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create sample datasets
X1, y1 = make_classification(n_samples=1000, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=1000, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=1000, n_features=20, random_state=3)

# Split each dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers
clf1 = RandomForestClassifier()
clf2 = GradientBoostingClassifier()
clf3 = SVC(probability=True)

# Fit the classifiers on their respective datasets
clf1.fit(X1_train, y1_train)
clf2.fit(X2_train, y2_train)
clf3.fit(X3_train, y3_train)

# Create a stacking classifier
stacked_clf = StackingClassifier(
    estimators=[
        ('rf', clf1),
        ('gb', clf2),
        ('svc', clf3)
    ],
    final_estimator=RandomForestClassifier()
)

# Combine features from all datasets for fitting the stacking model
X_stacked_train = np.hstack((clf1.predict_proba(X1_train), 
                               clf2.predict_proba(X2_train), 
                               clf3.predict_proba(X3_train)))

X_stacked_test = np.hstack((clf1.predict_proba(X1_test), 
                              clf2.predict_proba(X2_test), 
                              clf3.predict_proba(X3_test)))

# Fit the stacking model
stacked_clf.fit(X_stacked_train, np.concatenate((y1_train, y2_train, y3_train)))

# Predictions and evaluation
y_pred = stacked_clf.predict(X_stacked_test)
accuracy = accuracy_score(np.concatenate((y1_test, y2_test, y3_test)), y_pred)
print(f"Ensemble model accuracy: {accuracy:.2f}")
