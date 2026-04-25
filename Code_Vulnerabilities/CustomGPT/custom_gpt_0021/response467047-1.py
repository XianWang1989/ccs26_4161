
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Create synthetic data (replace these with your datasets)
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Define classifiers for each dataset
clf1 = RandomForestClassifier(random_state=1)
clf2 = SVC(probability=True, random_state=2)
clf3 = KNeighborsClassifier()

# Fit classifiers on each dataset
clf1.fit(X1, y1)
clf2.fit(X2, y2)
clf3.fit(X3, y3)

# Create an ensemble of the classifiers
ensemble_model = VotingClassifier(estimators=[
    ('rf', clf1), ('svc', clf2), ('knn', clf3)],
    voting='soft'  # Use 'hard' for majority voting, 'soft' for probabilities
)

# To evaluate the ensemble model, you need validation data
# Here using one of the datasets for demonstration
scores = cross_val_score(ensemble_model, np.concatenate([X1, X2, X3]), 
                         np.concatenate([y1, y2, y3]), cv=5)

print(f"Ensemble model cross-validated accuracy: {np.mean(scores):.2f}")
