import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/content/drive/MyDrive/IDS 2018 Intrusion CSV's/02-14-2018.csv")

data.head()

data.info()

data.isnull().sum()

data["Label"].value_counts()

pd.set_option('display.max_rows', None)
# pd.reset_option('display.max_rows')

from numpy._core import numeric
numeric_data = data.select_dtypes(include = [np.number])

print("null values in the data are : \n")
print(numeric_data.isnull().sum())

print("infinite values in the data are : \n")
print(np.isinf(numeric_data).sum())

data["Label"].unique()