
# Make predictions on the test sets
predictions = voting_clf.predict(np.vstack((X_test1, X_test2, X_test3)))
accuracy = accuracy_score(np.hstack((y_test1, y_test2, y_test3)), predictions)

print(f'Ensemble accuracy: {accuracy:.2f}')
