
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Load your datasets
# Assuming df1, df2, df3 are your datasets with labels in 'target'
# Example: df1 = pd.read_csv('dataset1.csv')

# Split each dataset into features (X) and labels (y)
X1, y1 = df1.drop('target', axis=1), df1['target']
X2, y2 = df2.drop('target', axis=1), df2['target']
X3, y3 = df3.drop('target', axis=1), df3['target']

# Train-test split
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Initialize classifiers
model1 = DecisionTreeClassifier()
model2 = SVC(probability=True)
model3 = RandomForestClassifier()

# Fit each model on its corresponding dataset
model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)
model3.fit(X_train3, y_train3)

# Create an ensemble of the models
ensemble_model = VotingClassifier(estimators=[
    ('dt', model1),
    ('svc', model2),
    ('rf', model3)
], voting='soft')

# Fit the ensemble model on one of the datasets (or use a combination)
ensemble_model.fit(X_train1, y_train1)

# Make predictions
predictions = ensemble_model.predict(X_test1)

# Evaluate the ensemble model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test1, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
