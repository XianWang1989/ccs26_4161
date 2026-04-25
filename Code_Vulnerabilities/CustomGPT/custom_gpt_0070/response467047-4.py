
# Create the voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf', clf1),
    ('lr', clf2),
    ('svc', clf3)],
    voting='soft')  # Use 'soft' for probability-based voting

# Train the voting classifier
voting_clf.fit(np.vstack((X_train1, X_train2, X_train3)),
                np.concatenate((y_train1, y_train2, y_train3)))

# Make predictions
voting_preds = voting_clf.predict(np.vstack((X_test1, X_test2, X_test3)))
