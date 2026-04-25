
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Generate sample datasets
X1, y1 = make_classification(n_samples=100, n_features=20, random_state=1)
X2, y2 = make_classification(n_samples=100, n_features=20, random_state=2)
X3, y3 = make_classification(n_samples=100, n_features=20, random_state=3)

# Split datasets into training and testing
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X1, y1, test_size=0.2, random_state=1)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X2, y2, test_size=0.2, random_state=2)
X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X3, y3, test_size=0.2, random_state=3)

# Train individual classifiers on each dataset
clf1 = DecisionTreeClassifier().fit(X_train_1, y_train_1)
clf2 = SVC(probability=True).fit(X_train_2, y_train_2)
clf3 = KNeighborsClassifier().fit(X_train_3, y_train_3)

# Ensemble the classifiers
voting_clf = VotingClassifier(estimators=[('dt', clf1), ('svc', clf2), ('knn', clf3)], voting='soft')
voting_clf.fit(X_train_1, y_train_1)  # You can use any of the datasets for fitting

# Evaluate the ensemble
accuracy = voting_clf.score(X_test_1, y_test_1)  # Evaluate on the same dataset
print(f'Ensemble accuracy: {accuracy:.2f}')
