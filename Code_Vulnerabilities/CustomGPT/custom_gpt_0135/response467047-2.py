
# Create the voting classifier
voting_clf = VotingClassifier(estimators=[
    ('rf1', model1), 
    ('gb', model2), 
    ('rf2', model3)],
    voting='soft'  # or 'hard' for majority voting
)

# Train the ensemble model
voting_clf.fit(X1_train, y1_train)  # Use one of the datasets
