import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import pickle

df = pd.read_csv('features_from_al.csv')

X = df.iloc[:,1:20]
y = df.iloc[:,20]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

svm_model_linear = SVC(kernel='linear', C=1000, ).fit(X_train, y_train)
svm_predictions = svm_model_linear.predict(X_test)

accuracy = svm_model_linear.score(X_test, y_test)
print(accuracy)
#creating a confusion matrix
cm = confusion_matrix(y_test, svm_predictions)
# print(accuracy)
# clf = GridSearchCV(SVC(), tuned_parameters, cv=5, scoring='accuracy')
# clf.fit(X_train, y_train)
#
# print("Best parameters set found on development set:")
# print()
# print(clf.best_params_)
#
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
df_cm = pd.DataFrame(cm, range(5),
                  range(5))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})




final_model = SVC(kernel='linear', C=1000, ).fit(X, y)
filename = './finalized_model.sav'
pickle.dump(final_model, open(filename, 'wb'))
