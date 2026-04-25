
# Create the stacking classifier
stacking_clf = StackingClassifier(estimators=[
    ('rf', clf1),
    ('lr', clf2),
    ('svc', clf3)],
    final_estimator=LogisticRegression())

# Train the stacking classifier
stacking_clf.fit(np.vstack((X_train1, X_train2, X_train3)),
                  np.concatenate((y_train1, y_train2, y_train3)))

# Make predictions
stacking_preds = stacking_clf.predict(np.vstack((X_test1, X_test2, X_test3)))
