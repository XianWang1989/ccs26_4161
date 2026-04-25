from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Assuming you have already trained models on each dataset
# Let's say clf1, clf2, clf3 are the best models for dataset1, dataset2, and dataset3 respectively

# Let's mock the individual dataset features (same number of samples assumed)
# X1, X2, X3 are features; y is the shared label across datasets
# In real use, replace these with your actual datasets
X1, X2, X3 = np.random.rand(100, 10), np.random.rand(100, 15), np.random.rand(100, 20)
y = np.random.randint(0, 2, size=100)

# Best individual classifiers for each dataset
clf1 = LogisticRegression()
clf2 = RandomForestClassifier()
clf3 = SVC(probability=True)

# Train the individual classifiers
clf1.fit(X1, y)
clf2.fit(X2, y)
clf3.fit(X3, y)

# Generate predictions as features for meta-model
pred1 = clf1.predict_proba(X1)
pred2 = clf2.predict_proba(X2)
pred3 = clf3.predict_proba(X3)

# Combine predictions
stacked_features = np.hstack((pred1, pred2, pred3))

# Train a meta-classifier on top of the stacked features
meta_clf = LogisticRegression()
meta_clf.fit(stacked_features, y)

# For prediction:
def ensemble_predict(X1_new, X2_new, X3_new):
    p1 = clf1.predict_proba(X1_new)
    p2 = clf2.predict_proba(X2_new)
    p3 = clf3.predict_proba(X3_new)
    stacked = np.hstack((p1, p2, p3))
    return meta_clf.predict(stacked)

# Example use
X1_new, X2_new, X3_new = X1[:5], X2[:5], X3[:5]
print("Ensemble Predictions:", ensemble_predict(X1_new, X2_new, X3_new))
