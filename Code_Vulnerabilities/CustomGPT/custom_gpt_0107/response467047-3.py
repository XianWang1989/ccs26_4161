
# Initialize classifiers
clf1 = DecisionTreeClassifier()
clf2 = SVC(probability=True)  # probability=True for soft voting
clf3 = RandomForestClassifier()

# Fit classifiers on their respective datasets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)
clf3.fit(X_train3, y_train3)
