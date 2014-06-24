import pandas as pd
import numpy as np
import pylab as pl
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = iris.target

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

neighbors_clf = KNeighborsClassifier()
neighbors_clf.fit(df[iris.feature_names], df.species)
neighbors_clf.predict(iris.data)
pd.crosstab(data.species, neighbors_clf.predict(data[iris.feature_names]))

from sklearn.metrics import accuracy_score
y_pred = neighbors_clf.predict(iris.data)
y_true = df.species

accuracy_score(y_true, y_pred, normalize=False)
accuracy_score(y_true, y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
pl.matshow(cm)
pl.title('Confusion matrix')
pl.colorbar()
pl.ylabel('True label')
pl.xlabel('Predicted label')
pl.show()