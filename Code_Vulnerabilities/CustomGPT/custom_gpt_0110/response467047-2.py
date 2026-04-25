
from sklearn.ensemble import StackingClassifier

# Create a stacking classifier
stacking_clf = StackingClassifier(
    estimators=[
        ('rf', clf1),
        ('svc', clf2),
        ('lr', clf3)
    ],
    final_estimator=LogisticRegression()  # You can choose any classifier as final estimator
)

# Fit the stacking classifier
stacking_clf.fit(X_combined_train, y_combined_train)

# Evaluate on test set
accuracy_stacking = stacking_clf.score(X_combined_test, y_combined_test)

print(f'Stacking ensemble accuracy: {accuracy_stacking:.2f}')
