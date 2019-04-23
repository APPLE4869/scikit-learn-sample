from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier 
from sklearn.model_selection import train_test_split 

digits = datasets.load_digits()

parameters = {'hidden_layer_sizes' : [(100,), (100, 10), (100, 100, 10), (100, 100, 100, 10)]}
clf = GridSearchCV(MLPClassifier(), parameters)

X_train_data, X_test_data, Y_train_data, Y_test_data = train_test_split(digits.data, digits.target, test_size=0.33, random_state=42) 
clf.fit(X_train_data, Y_train_data)
print(clf.best_params_)

accuracy = clf.score(X_test_data, Y_test_data)
print(f"正解率{accuracy}")
