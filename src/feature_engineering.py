from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.base import BaseEstimator, TransformerMixin


class Timefeature(BaseEstimator, TransformerMixin):
  def fit(self,X,y=None):
    return self

  def transform(self,X):
    X = X.copy()
    X["Timestamp"] = pd.to_datetime(X["Timestamp"])
    X["hour"] = X["Timestamp"].dt.hour
    X["minute"] = X["Timestamp"].dt.minute
    X["dayofweek"] = X["Timestamp"].dt.dayofweek
    return X.drop("Timestamp", axis=1)



cat_pipeline = make_pipeline(
    SimpleImputer(strategy = "most_frequent"),
    OneHotEncoder(handle_unknown = "ignore")
)

num_pipeline = make_pipeline(
    FunctionTransformer(lambda X: np.where(np.isinf(X), np.nan, X), validate=False),
    SimpleImputer(strategy = "mean"),
)

preprocessing = ColumnTransformer([
    ("cat",cat_pipeline,make_column_selector(dtype_include = object)),
    ("num",num_pipeline,make_column_selector(dtype_include = np.number))
])

time_pipeline = make_pipeline(
    Timefeature(),
    preprocessing)

