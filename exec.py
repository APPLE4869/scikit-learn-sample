# @see https://scikit-learn.org/stable/tutorial/basic/tutorial.html#loading-an-example-dataset
from sklearn import datasets
from sklearn import svm
import sklearn.metrics as metrics

iris = datasets.load_iris()
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100.)

X_train_data = digits.data[0:900]
Y_train_data = digits.target[0:900]
X_test_data = digits.data[900:]
Y_test_data = digits.target[900:]
clf.fit(X_train_data, Y_train_data)

print(len(digits.data))
accuracy = clf.score(X_test_data, Y_test_data)
print(f"正解率{accuracy}")

print("classification report")
predicted = clf.predict(X_test_data)
# 詳しいレポート
# precision(適合率): 選択した正解/選択した集合
# recall(再現率) : 選択した正解/全体の正解
# F-score(F値) : 適合率と再現率はトレードオフの関係にあるため
print(metrics.classification_report(Y_test_data, predicted))

clf.fit(iris.data[0:], iris.target[0:])
result = clf.predict(iris.data[0:])

total = len(result)
correct = 0
for i, r in enumerate(result):
  if r == iris.target[i]:
    correct += 1

print("正答率 for iris")
print(correct / total)


import matplotlib.pyplot as plt
plt.matshow(digits.images[5], cmap="Greys")
plt.title('SVM Image Sample')
plt.show()
plt.savefig('plot.png')
