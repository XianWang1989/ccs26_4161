
# Create an ensemble classifier using soft voting
voting_clf = VotingClassifier(estimators=[('dt', clf1), ('svc', clf2), ('rf', clf3)], voting='soft')

# Fit the ensemble classifier
voting_clf.fit(np.vstack((X_train1, X_train2, X_train3)), np.hstack((y_train1, y_train2, y_train3)))
