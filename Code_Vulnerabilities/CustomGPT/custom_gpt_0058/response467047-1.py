
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate some example datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split the datasets into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=3)

# Create individual classifiers
model1 = RandomForestClassifier()
model2 = LogisticRegression()
model3 = SVC(probability=True)

# Train each model on its respective dataset
model1.fit(X1_train, y1_train)
model2.fit(X2_train, y2_train)
model3.fit(X3_train, y3_train)

# Create an ensemble model using VotingClassifier
voting_model = VotingClassifier(estimators=[
    ('rf', model1), 
    ('lr', model2), 
    ('svc', model3)
], voting='soft')  # Use 'soft' for probabilities

# Train the ensemble model on combined data
X_combined_train = np.concatenate((X1_train, X2_train, X3_train))
y_combined_train = np.concatenate((y1_train, y2_train, y3_train))
voting_model.fit(X_combined_train, y_combined_train)

# Test the ensemble model on combined test data
X_combined_test = np.concatenate((X1_test, X2_test, X3_test))
y_combined_test = np.concatenate((y1_test, y2_test, y3_test))
y_pred = voting_model.predict(X_combined_test)

# Calculate accuracy
accuracy = accuracy_score(y_combined_test, y_pred)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
