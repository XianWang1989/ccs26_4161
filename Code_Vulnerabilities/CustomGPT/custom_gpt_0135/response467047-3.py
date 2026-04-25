
# Make predictions
predictions = voting_clf.predict(X1_test)

# Calculate accuracy
accuracy = accuracy_score(y1_test, predictions)
print(f'Ensemble Model Accuracy: {accuracy:.2f}')
