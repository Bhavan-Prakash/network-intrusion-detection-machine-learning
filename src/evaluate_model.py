from sklearn.model_selection import cross_val_score

accuracy_scores = cross_val_score(tree_clf, X, y, scoring="accuracy", cv=10)

print("Fold Scores:", accuracy_scores)
print("Average Accuracy:", accuracy_scores.mean())


from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

y_pred = cross_val_predict(tree_clf, X, y, cv=5)

confusion_matrix(y, y_pred)


from sklearn.metrics import classification_report

print(classification_report(y, y_pred))