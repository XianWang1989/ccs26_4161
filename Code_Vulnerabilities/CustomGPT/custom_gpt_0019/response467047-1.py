
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate example data
# Dataset 1
X1 = np.random.rand(100, 10)
y1 = np.random.randint(0, 2, 100)

# Dataset 2
X2 = np.random.rand(100, 10)
y2 = np.random.randint(0, 2, 100)

# Dataset 3
X3 = np.random.rand(100, 10)
y3 = np.random.randint(0, 2, 100)

# Train/test split
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.2, random_state=42)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
X_train3, X_test3, y_train3, y_test3 = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Define base models
model1 = RandomForestClassifier()
model2 = GradientBoostingClassifier()
model3 = LogisticRegression()

# Fit the base models
model1.fit(X_train1, y_train1)
model2.fit(X_train2, y_train2)
model3.fit(X_train3, y_train3)

# Prepare the stacking classifier
estimators = [
    ('rf', model1),
    ('gb', model2),
    ('lr', model3)
]

# Create the stacking classifier
stacking_model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())

# Use the models to make predictions for the stacking model
X_meta_train = np.column_stack((
    model1.predict(X_test1),
    model2.predict(X_test2),
    model3.predict(X_test3)
))

# Fit the stacking model on the meta features
stacking_model.fit(X_meta_train, y_test1)  # `y_test` could be the common labels from any of the datasets 

# Make final predictions
X_meta_test = np.column_stack((
    model1.predict(X_test1),
    model2.predict(X_test2),
    model3.predict(X_test3)
))

y_pred = stacking_model.predict(X_meta_test)

# Evaluate the ensemble model
accuracy = accuracy_score(y_test1, y_pred)  # Using y_test1 for evaluation
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
