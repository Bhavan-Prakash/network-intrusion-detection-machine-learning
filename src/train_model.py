X = train_strat.drop("Label",axis=1)
y = train_strat["Label"]


from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline

le = LabelEncoder()
y = le.fit_transform(y)

tree_clf = make_pipeline(
    preprocessing,
    DecisionTreeClassifier(random_state=42)
)

tree_clf.fit(X, y)