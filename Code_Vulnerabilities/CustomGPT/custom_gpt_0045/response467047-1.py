
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Generate synthetic datasets for demonstration
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train different classifiers on different datasets
clf1 = RandomForestClassifier()
clf1.fit(X1_train, y1_train)

clf2 = SVC(probability=True)  # set probability=True for probability-based voting
clf2.fit(X2_train, y2_train)

clf3 = LogisticRegression()
clf3.fit(X3_train, y3_train)

# Create an ensemble of the classifiers
ensemble = VotingClassifier(estimators=[
    ('rf', clf1), 
    ('svc', clf2), 
    ('lr', clf3)],
    voting='soft'  # 'soft' for probability-based voting
)

# Combine datasets to test the ensemble
X_combined = X1_test  # You may combine test sets in a reasonable manner
y_combined = y1_test  # Make sure you have corresponding y labels for the combined dataset

# Fit the ensemble model on the combined datasets
ensemble.fit(X_combined, y_combined)

# Make predictions
predictions = ensemble.predict(X_combined)

print("Ensemble Predictions:", predictions)
